# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

import unittest
from adt.priorityqueue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def test_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.isEmpty())
        pq.insert(0)
        self.assertFalse(pq.isEmpty())
        pq.max()
        self.assertFalse(pq.isEmpty())
        pq.popMax()
        self.assertTrue(pq.isEmpty())

    def test_size(self):
        pq = PriorityQueue()
        self.assertEqual(pq.count(), 0)
        pq.insert(1)
        self.assertEqual(pq.count(), 1)
        pq.insert(2)
        self.assertEqual(pq.count(), 2)
        pq.max()
        self.assertEqual(pq.count(), 2)
        pq.popMax()
        pq.popMax()
        self.assertEqual(pq.count(), 0)

    def test_insert(self):
        pq = PriorityQueue()
        self.assertEqual(pq.__str__(), [0])
        pq.insert(1)
        pq.insert(2)
        pq.insert(4)
        self.assertEqual(pq.__str__(), [0, 4, 1, 2])

    def test_max(self):
        pq = PriorityQueue()
        self.assertEqual(pq.max(), None)
        pq.insert(1)
        pq.insert(3)
        pq.insert(33)
        pq.insert(8)
        self.assertEqual(pq.max(), 33)

    def test_pop(self):
        pq = PriorityQueue()
        self.assertEqual(pq.popMax(), None)
        for i in range(10):
            pq.insert(i)
        self.assertEqual(pq.popMax(), 9)
        pq.insert(19)
        self.assertEqual(pq.popMax(), 19)
        print(pq.__str__())

    def test_build(self):
        pq = PriorityQueue()
        pq.buildHeap([1, 2, 3, 4, 5])
        self.assertEqual(pq.max(), 5)
        pq.buildHeap([12, 2, 44, 11])
        self.assertEqual(pq.popMax(), 44)
        pq.insert(55)
        self.assertEqual(pq.popMax(), 55)

if __name__ == "__main__":
    unittest.main()
