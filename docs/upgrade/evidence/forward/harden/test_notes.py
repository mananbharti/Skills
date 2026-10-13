import os,unittest
from unittest.mock import patch
import notes

class Boundary(unittest.TestCase):
    def setUp(self): notes.seed()
    def test_owner_reads(self):
        self.assertEqual(len(notes.get_note('amy',1)),1)
        self.assertEqual(notes.get_note('bob',1),[])
    def test_injection(self):
        self.assertEqual(notes.get_note('amy', '1 OR 1=1'),[])
        self.assertEqual(notes.get_note("amy' OR 1=1 --",1),[])
    def test_delete_scope(self):
        self.assertFalse(notes.delete_note('bob',1))
        self.assertEqual(len(notes.get_note('amy',1)),1)
        self.assertTrue(notes.delete_note('amy',1))
        self.assertEqual(notes.get_note('amy',1),[])
        self.assertFalse(notes.delete_note('amy',1))
    def test_delete_injection(self):
        self.assertFalse(notes.delete_note('amy','1 OR 1=1'))
        self.assertEqual(len(notes.get_note('bob',2)),1)
    def test_configuration(self):
        with patch.dict(os.environ,{},clear=True):
            with self.assertRaises(RuntimeError): notes.get_secret()
        with patch.dict(os.environ,{'NOTES_SECRET':''},clear=True):
            with self.assertRaises(RuntimeError): notes.get_secret()
        with patch.dict(os.environ,{'NOTES_SECRET':'synthetic-test-only'},clear=True):
            self.assertEqual(notes.get_secret(),'synthetic-test-only')

if __name__=='__main__': unittest.main()
