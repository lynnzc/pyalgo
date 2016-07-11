# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

import unittest
from adt.stack import Stack


class TestStackCase(unittest.TestCase):

    def test_peek(self):
        s = Stack()
        s.push(1)
        self.assertEqual(s.peek(), 1)
        index = [1, 2, 3, 4, 5]
        for i in index:
            s.push(i)
        self.assertEqual(s.peek(), index[-1])

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        index = 10
        for i in range(index):
            s.push(i)
        self.assertEqual(s.size(), index)
        for i in range(5):
            s.pop()
        self.assertEqual(s.size(), index - 5)

    def test_is_empty(self):
        s = Stack()
        self.assertTrue(s.isEmpty())
        s.push(1)
        self.assertFalse(s.isEmpty())

if __name__ == "__main__":
    unittest.main()
