# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

import unittest
from adt.deque import Deque


class TestDequeCase(unittest.TestCase):

    def test_size(self):
        d = Deque()
        self.assertEqual(d.size(), 0)
        d.enqueueFront(1)
        d.enqueueRear(2)
        self.assertEqual(d.size(), 2)

    def test_empty(self):
        d = Deque()
        self.assertTrue(d.isEmpty())
        d.enqueueFront(1)
        self.assertFalse(d.isEmpty())

    def test_str(self):
        d = Deque()
        self.assertEqual(d.__str__(), [])
        d.enqueueFront(1)
        d.enqueueRear(2)
        self.assertEqual(d.__str__(), [1, 2])
        d.enqueueFront(3)
        self.assertEqual(d.__str__(), [3, 1, 2])
        d.enqueueRear(4)
        self.assertEqual(d.__str__(), [3, 1, 2, 4])
        d.dequeueFront()
        self.assertEqual(d.__str__(), [1, 2, 4])
        d.dequeueRear()
        d.dequeueRear()
        self.assertEqual(d.__str__(), [1])

if __name__ == "__main__":
    unittest.main()
