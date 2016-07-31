# !/usr/bin/python
# -*- coding: utf-8 -*-


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    # return the height of bst
    def height(self):
        if self.root is None:
            return 0
        else:
            return self.root.height()

    # return whether the bst is empty or not
    def isEmpty(self):
        return (self.size == 0)

    # insert a new node to bst
    def insert(self, key):
        if self.root is None:
            self.root = self.TreeNode(key)
        else:
            self.root.insert(key)

        self.size += 1

    # return whether the key exists in the bst or not
    def find(self, key):
        if self.root is None:
            return False
        else:
            return self.root.find(key)

    # delete a node
    def delete(self, key):
        if self.root is not None:
            isDeleted = False
            self.root, isDeleted = self.root.delete(key, None)
            if isDeleted:
                self.size -= 1
                return True
        return False

    # print
    def printTree(self):
        if self.root is None:
            print('empty tree', end=' ')
        else:
            self.root.printTree()
        print("")

    def count(self):
        return self.size

    class TreeNode:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def height(self):
            if self is None:
                return 0
            elif self.left is None and self.right is None:
                # leaf node
                return 1
            elif self.left is None:
                return self.right.height() + 1
            elif self.right is None:
                return self.left.height() + 1
            else:
                # two child nodes
                return max(self.left.height(), self.right.height()) + 1

        def getKey(self):
            return self.key

        # insert a new node to the bst,
        # using this node as the root
        def insert(self, key):
            # allow duplicate key
            if self.getKey() <= key:
                if self.left is None:
                    self.left = BinarySearchTree.TreeNode(key)
                else:
                    self.left.insert(key)
            else:
                # self.getKey() > key
                if self.right is None:
                    self.right = BinarySearchTree.TreeNode(key)
                else:
                    self.right.insert(key)

        # return whether the key exists or not
        def find(self, key):
            if self.getKey() == key:
                return True
            elif self.getKey() < key and self.left is not None:
                return self.left.find(key)
            elif self.getKey() > key and self.right is not None:
                return self.right.find(key)
            return False

        # delete a node
        def delete(self, key, parent):
            root = None
            if parent is None:
                root = self

            if self.getKey() == key:
                # if this node has no child nodes
                if self.left is None and self.right is None:
                    if parent is not None:
                        # this node is not the root
                        if parent.left is self:
                            parent.left = None
                        else:
                            # parent.right is self
                            parent.right = None
                    else:
                        # this node is root, just set to None
                        root = None
                elif self.left is None:
                    # only right
                    if parent is not None:
                        if parent.right is self:
                            parent.right = self.right
                        else:
                            # parent.left is self:
                            parent.left = self.right
                    else:
                        # root
                        root = self.right
                elif self.right is None:
                    # only left
                    if parent is not None:
                        if parent.right is self:
                            parent.right = self.left
                        else:
                            # parent.left is self
                            parent.left = self.left
                    else:
                        # root
                        root = self.left
                else:
                    # has two child nodes

                    # find its successor node
                    p = self
                    successor = self.right
                    while(successor.left is not None):
                        p = successor
                        successor = successor.left

                    # remove the successor
                    if p.left is successor:
                        p.left = successor.right
                    else:
                        # p.right is successor
                        p.right = successor.right

                    # replace the key
                    self.key = successor.getKey()

                return root, True
            elif self.getKey() > key and self.right is not None:
                return self.right.delete(key, self)
            elif self.getKey() < key and self.left is not None:
                return self.left.delete(key, self)
            return root, False

        # print inorider traversal keys of the bst
        def printTree(self):
            if self.left is not None:
                self.left.printTree()

            print(str(self.getKey()), end=' ')

            if self.right is not None:
                self.right.printTree()
