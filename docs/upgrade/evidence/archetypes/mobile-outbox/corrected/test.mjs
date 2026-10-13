import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { flush } from './outbox.mjs';

function store(t) {
  const dir = mkdtempSync(join(tmpdir(), 'outbox-case-'));
  t.after(() => rmSync(dir, { recursive: true, force: true }));
  const path = join(dir, 'queue.json');
  const result = {
    read: () => JSON.parse(readFileSync(path, 'utf8')),
    write: operations => writeFileSync(path, JSON.stringify(operations)),
  };
  result.write([{ id: 'op-1', tenant: 'alpha', text: 'draft' }]);
  return result;
}

test('unknown acknowledgment retains persisted operation for restart/retry', async t => {
  const queue = store(t);
  await assert.rejects(flush(queue, async () => { throw new Error('connection lost'); }));
  assert.equal(queue.read().length, 1);
  assert.equal(queue.read()[0].id, 'op-1');
});

test('retry uses stable business identity after server commits but ack is lost', async t => {
  const queue = store(t), effects = new Set(), attempts = [];
  let first = true;
  const send = async operation => {
    attempts.push(operation.id);
    effects.add(operation.id); // Synthetic server idempotency, not a provider API.
    if (first) { first = false; throw new Error('ack lost after commit'); }
  };
  await assert.rejects(flush(queue, send));
  await flush(queue, send);
  assert.deepEqual(attempts, ['op-1', 'op-1']);
  assert.equal(effects.size, 1);
  assert.deepEqual(queue.read(), []);
});
