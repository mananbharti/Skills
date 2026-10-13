import importlib.util,unittest,sqlite3
spec=importlib.util.spec_from_file_location('payment','payment-demo.py'); p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)

def event(id='e1',state='paid',tenant='alpha',order='order-1'):
    return dict(id=id,state=state,tenant=tenant,order=order)

class Boundaries(unittest.TestCase):
    def setUp(self): self.db=p.open_store(); self.addCleanup(self.db.close)
    def state(self): return self.db.execute("SELECT state FROM orders WHERE id='order-1'").fetchone()[0]
    def count(self,table): return self.db.execute('SELECT count(*) FROM '+table).fetchone()[0]
    def test_retries_and_distinct_events(self):
        p.apply_event(self.db,event()); p.apply_event(self.db,event()); p.apply_event(self.db,event('e2'))
        self.assertEqual(self.count('fulfillments'),1)
        self.assertEqual(self.state(),'paid')
    def test_stale_pending_then_refund(self):
        p.apply_event(self.db,event()); p.apply_event(self.db,event('e2','pending'))
        self.assertEqual(self.state(),'paid')
        p.apply_event(self.db,event('e3','refunded')); self.assertEqual(self.state(),'refunded')
        p.apply_event(self.db,event('e4','paid')); self.assertEqual(self.state(),'refunded')
        self.assertEqual(self.count('fulfillments'),1)
    def test_wrong_tenant(self):
        with self.assertRaises(PermissionError): p.apply_event(self.db,event(tenant='beta'))
        self.assertEqual(self.state(),'pending'); self.assertEqual(self.count('receipts'),0)
    def test_missing_order(self):
        with self.assertRaises(LookupError): p.apply_event(self.db,event(order='missing'))
        self.assertEqual(self.count('receipts'),0)
    def test_out_of_order_refund_retry(self):
        refund=event('refund','refunded')
        with self.assertRaises(ValueError): p.apply_event(self.db,refund)
        self.assertEqual(self.count('receipts'),0)
        p.apply_event(self.db,event()); p.apply_event(self.db,refund)
        self.assertEqual(self.state(),'refunded')
    def test_invalid_state_and_reused_identity(self):
        with self.assertRaises(ValueError): p.apply_event(self.db,event(state='unknown'))
        p.apply_event(self.db,event())
        with self.assertRaises(ValueError): p.apply_event(self.db,event(state='refunded'))
        self.assertEqual(self.state(),'paid')
    def test_atomic_failure_then_retry(self):
        self.db.execute("CREATE TRIGGER fail BEFORE INSERT ON fulfillments BEGIN SELECT RAISE(ABORT,'synthetic fault'); END")
        with self.assertRaises(sqlite3.IntegrityError): p.apply_event(self.db,event())
        self.assertEqual(self.state(),'pending'); self.assertEqual(self.count('receipts'),0)
        self.db.execute('DROP TRIGGER fail'); p.apply_event(self.db,event())
        self.assertEqual(self.count('fulfillments'),1)
    def test_outer_transaction_owned_by_caller(self):
        self.db.execute('BEGIN'); p.apply_event(self.db,event()); self.db.rollback()
        self.assertEqual(self.state(),'pending'); self.assertEqual(self.count('receipts'),0)

if __name__=='__main__': unittest.main()
