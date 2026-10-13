import test from 'node:test';
import assert from 'node:assert/strict';
import { apply } from './input.mjs';

const make = () => ({ players: {
  alice: { x: 0, last: 0, epoch: 'session-2' },
  bob: { x: 0, last: 0, epoch: 'session-1' },
} });
const command = patch => ({ player: 'alice', dx: 1, sequence: 1, epoch: 'session-2', ...patch });

test('repeated command changes server state once', () => {
  const state = make();
  assert.equal(apply(state, 'alice', command()), 'applied');
  assert.equal(apply(state, 'alice', command()), 'duplicate');
  assert.equal(state.players.alice.x, 1);
});
test('authenticated principal cannot command another player', () => {
  const state = make(), before = structuredClone(state);
  assert.throws(() => apply(state, 'alice', command({ player: 'bob', epoch: 'session-1' })));
  assert.deepEqual(state, before);
});
test('old-session replay and sequence gap require resync without mutation', () => {
  const state = make(), before = structuredClone(state);
  assert.throws(() => apply(state, 'alice', command({ epoch: 'session-1' })));
  assert.throws(() => apply(state, 'alice', command({ sequence: 3 })));
  assert.deepEqual(state, before);
  assert.equal(apply(state, 'alice', command()), 'applied');
  assert.equal(apply(state, 'alice', command({ sequence: 2, dx: -1 })), 'applied');
  assert.equal(state.players.alice.x, 0);
});
test('client movement limit is enforced at the server boundary', () => {
  const state = make();
  for (const dx of [100, NaN, Infinity, '1', 0.5]) {
    assert.throws(() => apply(state, 'alice', command({ dx })));
  }
  assert.equal(state.players.alice.x, 0);
});
