# !/usr/bin/python
# coding:utf-8


class BinaryTree:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = None
        self.right = None

    # insert a new node as a left child of the tree
    def insertLeft(self, value):
        if self.left is None:
            self.left = BinaryTree(value)
        else:
            leftTree = BinaryTree(value)
            leftTree.left = self.left
            self.left = leftTree

    # insert a new node as a right child of the tree
    def insertRight(self, value):
        if self.right is None:
            self.right = BinaryTree(value)
        else:
            rightTree = BinaryTree(value)
            rightTree.right = self.right
            self.right = rightTree

    # return the left child
    def getLeft(self):
        return self.left

    # return the right child
    def getRight(self):
        return self.right

    # return the value of the tree
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    # return the height of the tree
    def height(self):
        if self is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.height() + 1
        elif self.right is None:
            return self.left.height() + 1
        else:
            return max(self.left.height(), self.right.height()) + 1
