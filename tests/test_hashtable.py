# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

import unittest

from adt.hashtable import HashTable


class TestHashTableCase(unittest.TestCase):
    def test_empty(self):
        ht = HashTable()
        self.assertTrue(ht.isEmpty())
        ht.put(1, "1")
        self.assertFalse(ht.isEmpty())
        ht.remove(1)
        self.assertTrue(ht.isEmpty())

    def test_count(self):
        ht = HashTable()
        self.assertEqual(ht.itemCount(), 0)
        ht.put(11, "11")
        self.assertEqual(ht.itemCount(), 1)
        ht.put(33, "33")
        self.assertEqual(ht.itemCount(), 2)
        ht.remove(33)
        self.assertEqual(ht.itemCount(), 1)
        isRemoved = ht.remove(13)
        if isRemoved:
            self.assertEqual(ht.itemCount(), 0)
        else:
            self.assertEqual(ht.itemCount(), 1)
        isRemoved = ht.remove(11)
        if isRemoved:
            self.assertEqual(ht.itemCount(), 0)
        else:
            self.assertEqual(ht.itemCount(), 1)

    def test_contain(self):
        ht = HashTable()
        self.assertFalse(ht.contains(11))
        ht.put(11, "11")
        self.assertTrue(ht.contains(11))
        ht.remove(11)
        self.assertFalse(ht.contains(11))

    def test_get(self):
        ht = HashTable()
        self.assertEqual(ht.get(1), None)
        ht.put(11, "11")
        self.assertEqual(ht.get(11), "11")
        self.assertFalse(ht.get(11) == 11)
        ht.put(22, "22")
        self.assertEqual(ht.get(22), "22")
        ht.remove(22)
        self.assertFalse(ht.get(22), None)
        print("\nget(11) is: %s" % (ht.get(11)))


if __name__ == "__main__":
    unittest.main()
