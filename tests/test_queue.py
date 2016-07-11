# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

import unittest
from adt.queue import Queue


class TestQueueCase(unittest.TestCase):

    def test_size(self):
        q = Queue()
        self.assertEqual(q.size(), 0)
        test_list = [1, 2, 3]
        for i in test_list:
            q.enqueue(i)
        self.assertEqual(q.size(), 3)

    def test_empty(self):
        q = Queue()
        self.assertTrue(q.isEmpty())
        q.enqueue(1)
        self.assertFalse(q.isEmpty())
        q.dequeue()
        self.assertTrue(q.isEmpty())

if __name__ == "__main__":
    unittest.main()
