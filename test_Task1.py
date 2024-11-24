import unittest
from Task1 import Dictionary

class TestDictionary(unittest.TestCase):
    def test_add_and_lookup_entry(self):
        d = Dictionary()
        d.newentry("Apple", "A fruit that grows on trees")
        self.assertEqual(d.look("Apple"), "A fruit that grows on trees")

    def test_lookup_nonexistent_entry(self):
        d = Dictionary()
        self.assertEqual(d.look("Banana"), "Can't find entry for Banana")

    def test_overwrite_entry(self):
        d = Dictionary()
        d.newentry("Apple", "A fruit that grows on trees")
        d.newentry("Apple", "A tech company")
        self.assertEqual(d.look("Apple"), "A tech company")

    def test_multiple_entries(self):
        d = Dictionary()
        d.newentry("Apple", "A fruit that grows on trees")
        d.newentry("Banana", "A long curved fruit")
        d.newentry("Cherry", "A small, round stone fruit")
        self.assertEqual(d.look("Apple"), "A fruit that grows on trees")
        self.assertEqual(d.look("Banana"), "A long curved fruit")
        self.assertEqual(d.look("Cherry"), "A small, round stone fruit")

if __name__ == '__main__':
    unittest.main()