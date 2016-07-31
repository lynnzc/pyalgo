# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

import unittest
from adt.list import List


class TestListCase(unittest.TestCase):
    def test_pop(self):
        l = List()
        test_list = [2, 33, 11, 4]
        for i in range(len(test_list)):
            l.insert(test_list[i], i)
        self.assertEqual(l.__str__(), [2, 33, 11, 4])
        self.assertEqual(l.pop(), 4)
        self.assertEqual(l.__str__(), [2, 33, 11])
        self.assertEqual(l.pop(), 11)
        self.assertEqual(l.pop(), 33)
        self.assertEqual(l.pop(), 2)
        self.assertEqual(l.__str__(), [])

    def test_remove(self):
        l = List()
        test_list = [4, 5, 6, 7, 8]
        for i in test_list:
            l.append(i)
        self.assertTrue(l.remove(8))
        self.assertEqual(l.__str__(), [4, 5, 6, 7])
        self.assertFalse(l.remove(8))
        self.assertFalse(l.remove(10))
        self.assertEqual(l.__str__(), [4, 5, 6, 7])

    def test_index(self):
        l = List()
        test_list = [1, 2, 4]
        for i in test_list:
            l.add(i)
        self.assertEqual(l.__str__(), [4, 2, 1])
        self.assertEqual(l.index(4), 0)
        self.assertEqual(l.index(3), -1)

    def test_find(self):
        l = List()
        test_list = [1, 2, 4, 55]
        for i in test_list:
            l.append(i)
        self.assertTrue(l.find(55))
        self.assertFalse(l.find(3))

    def test_add(self):
        l = List()
        self.assertEqual(l.__str__(), [])
        l.add(1)
        l.add(2)
        self.assertEqual(l.__str__(), [2, 1])

    def test_append(self):
        l = List()
        self.assertEqual(l.__str__(), [])
        l.append(1)
        self.assertEqual(l.__str__(), [1])
        l.append(2)
        self.assertEqual(l.__str__(), [1, 2])
        l.append(1)
        self.assertEqual(l.__str__(), [1, 2, 1])

    def test_size(self):
        l = List()
        self.assertEqual(l.size(), 0)
        l.append(1)
        self.assertEqual(l.size(), 1)
        l.remove(1)
        self.assertEqual(l.size(), 0)

    def test_empty(self):
        l = List()
        self.assertTrue(l.isEmpty())
        l.add(1)
        self.assertFalse(l.isEmpty())
        l.remove(1)
        self.assertTrue(l.isEmpty())

if __name__ == "__main__":
    unittest.main()
