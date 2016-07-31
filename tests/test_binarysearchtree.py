# !/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

import sys
sys.path.insert(0, '..')

from adt.binarysearchtree import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_height(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.height(), 0)
        bst.insert(0)
        self.assertEqual(bst.height(), 1)
        bst.insert(1)
        self.assertEqual(bst.height(), 2)
        bst.insert(-1)
        self.assertEqual(bst.height(), 2)
        bst.insert(2)
        self.assertEqual(bst.height(), 3)

    def test_size(self):
        bst = BinarySearchTree()
        self.assertEqual(bst.count(), 0)
        bst.insert(1)
        self.assertEqual(bst.count(), 1)
        bst.insert(1)
        self.assertEqual(bst.count(), 2)
        bst.delete(1)
        self.assertEqual(bst.count(), 1)
        bst.delete(1)
        self.assertEqual(bst.count(), 0)
        bst.insert(2)
        bst.delete(1)
        self.assertEqual(bst.count(), 1)

    def test_empty(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.isEmpty())
        bst.insert(0)
        self.assertFalse(bst.isEmpty())

    def test_print(self):
        bst = BinarySearchTree()
        bst.printTree()
        bst.insert(10)
        bst.insert(2)
        bst.insert(1)
        bst.insert(3)
        bst.insert(4)
        bst.printTree()

    def test_find(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.find(1))
        bst.insert(1)
        self.assertTrue(bst.find(1))
        self.assertFalse(bst.find(10))
        bst.delete(1)
        self.assertFalse(bst.find(1))

if __name__ == "__main__":
    unittest.main()
