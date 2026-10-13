"""Seeded local exercise, synthetic events only; deliberately unsafe, not production.

Copy this file into an isolated scratch workspace and implement the accepted
payment-event contract there. No network, provider account, or credentials.
The caller owns SQLite connection lifetime; persistence is observable in tables.
"""
import sqlite3


def open_store():
    db = sqlite3.connect(':memory:')
    db.executescript('''
        CREATE TABLE orders (id TEXT PRIMARY KEY, tenant TEXT, state TEXT);
        CREATE TABLE receipts (event_id TEXT PRIMARY KEY, order_id TEXT, tenant TEXT, state TEXT);
        CREATE TABLE fulfillments (order_id TEXT PRIMARY KEY, tenant TEXT NOT NULL);
        INSERT INTO orders VALUES ('order-1', 'alpha', 'pending');
        INSERT INTO orders VALUES ('order-2', 'beta', 'pending');
    ''')
    return db


def apply_event(db, event):
    """Synthetic preauthenticated ingress; caller owns any outer transaction.

    Contract: pending -> paid -> refunded. Late pending/paid is stale.
    A refund before paid is retryable and is not consumed. Provider identity
    is trusted by test precondition, but target ownership is checked locally.
    """
    if not isinstance(event, dict) or any(
        not isinstance(event.get(k), str) or not 0 < len(event[k]) <= 200
        for k in ('id', 'order', 'tenant', 'state')
    ) or event['state'] not in {'pending', 'paid', 'refunded'}:
        raise ValueError('invalid synthetic payment event')
    db.execute('SAVEPOINT payment_event')
    try:
        row = db.execute('SELECT tenant, state FROM orders WHERE id=?',
                         (event['order'],)).fetchone()
        if row is None:
            raise LookupError('unknown order')
        owner, current = row
        if event['tenant'] != owner:
            raise PermissionError('order tenant mismatch')
        identity = (event['order'], owner, event['state'])
        prior = db.execute('SELECT order_id,tenant,state FROM receipts WHERE event_id=?',
                           (event['id'],)).fetchone()
        if prior is not None:
            if prior != identity:
                raise ValueError('event identity reused with conflicting values')
            result = 'duplicate'
        else:
            desired = event['state']
            if desired == 'refunded' and current == 'pending':
                raise ValueError('refund precedes payment; retry or reconcile')
            advance = (current, desired) in {('pending', 'paid'), ('paid', 'refunded')}
            if advance:
                db.execute('UPDATE orders SET state=? WHERE id=? AND tenant=? AND state=?',
                           (desired, event['order'], owner, current))
                if desired == 'paid':
                    db.execute('INSERT INTO fulfillments VALUES (?,?)',
                               (event['order'], owner))
            db.execute('INSERT INTO receipts VALUES (?,?,?,?)', (event['id'], *identity))
            result = 'applied' if advance else 'unchanged'
        db.execute('RELEASE payment_event')
        return result
    except BaseException:
        db.execute('ROLLBACK TO payment_event')
        db.execute('RELEASE payment_event')
        raise


if __name__ == '__main__':
    with open_store() as connection:
        for event in [
            {'id': 'evt-1', 'order': 'order-1', 'tenant': 'alpha', 'state': 'paid'},
            {'id': 'evt-2', 'order': 'order-1', 'tenant': 'alpha', 'state': 'paid'},
            {'id': 'evt-3', 'order': 'order-1', 'tenant': 'alpha', 'state': 'pending'},
        ]:
            apply_event(connection, event)
        print('state:', connection.execute('SELECT state FROM orders WHERE id=?', ('order-1',)).fetchone()[0])
        print('fulfillments:', connection.execute('SELECT COUNT(*) FROM fulfillments').fetchone()[0])
