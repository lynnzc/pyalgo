# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

import unittest
from adt.binarytree import BinaryTree


class TestBinaryTreeCase(unittest.TestCase):
    def test_height(self):
        bt = BinaryTree(1)
        self.assertEqual(bt.height(), 1)
        bt.insertLeft(2)
        bt.insertLeft(1)
        bt.insertRight(1)
        self.assertEqual(bt.height(), 3)

    def test_getvalue(self):
        bt = BinaryTree(1)
        self.assertEqual(bt.getValue(), 1)

    def test_getLeft(self):
        bt = BinaryTree(1)
        self.assertEqual(bt.getLeft(), None)
        bt.insertLeft(2)
        self.assertTrue(bt.getLeft() is not None)
        self.assertEqual(bt.getLeft().getValue(), 2)

    def test_getRight(self):
        bt = BinaryTree(1)
        self.assertEqual(bt.getRight(), None)
        bt.insertLeft(2)
        self.assertFalse(bt.getRight() is not None)
        bt.insertRight(3)
        self.assertTrue(bt.getRight() is not None)
        self.assertEqual(bt.getRight().getValue(), 3)

    def test_setvalue(self):
        bt = BinaryTree(1)
        self.assertEqual(bt.getValue(), 1)
        bt.setValue(3)
        self.assertEqual(bt.getValue(), 3)

if __name__ == "__main__":
    unittest.main()
