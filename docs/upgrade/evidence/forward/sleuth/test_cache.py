import unittest
from cache import Cache

class Regression(unittest.TestCase):
    def test_read_replace_read(self):
        c=Cache(); c.set('x','old'); self.assertEqual(c.get('x'),'old')
        c.set('x','new'); self.assertEqual(c._store['x'],'new')
        self.assertEqual(c.get('x'),'new')
    def test_unwarmed_and_other_keys(self):
        c=Cache(); c.set('x',1); c.set('x',2); self.assertEqual(c.get('x'),2)
        c.set('y',3); c.get('y'); c.set('x',4); self.assertEqual(c.get('y'),3)
    def test_missing_and_falsey(self):
        c=Cache()
        with self.assertRaises(KeyError): c.get('missing')
        c.set('x',1); c.get('x'); c.set('x',None); self.assertIsNone(c.get('x'))
        c.set('x',False); self.assertIs(c.get('x'),False)

if __name__=='__main__': unittest.main()
