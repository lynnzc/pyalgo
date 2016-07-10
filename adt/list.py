# !/usr/bin/python
# coding:utf-8


class List:

    def __init__(self):
        # initial a list with a header
        self.header = None

    # return whether the list is empty or not
    def isEmpty(self):
        return (self.header is None)

    # return the number of nodes in the list
    def size(self):
        cur = self.header
        s = 0
        while cur is not None:
            s += 1
            cur = cur.next()
        return s

    # insert a node to the list at pos
    def insert(self, node, pos):
        if (0 > pos) or (pos > self.size()):
            # index out of bound
            return
        cur = self.header
        # find the position
        i = 0
        pre = None
        while (i < pos) and (cur is not None):
            pre = cur
            cur = cur.next()
            i += 1
        # allocate a new Node
        new = self.Node(node)
        new.setNext(cur)
        if pre is None:
            self.header = new
        else:
            pre.setNext(new)

    # insert a node to the end of the list
    def append(self, node):
        self.insert(node, self.size() - 1)

    # insert a node to the first of the list
    def add(self, node):
        self.insert(node, 0)

    # remove the node in the list if exists
    def remove(self, node):
        cur = self.header

        pre = None
        while cur is not None:
            if (cur.get() == node):
                # remove step
                if pre is None:
                    # remove the first node
                    self.header = cur.next()
                else:
                    # common case
                    pre.setNext(cur.next())
                    cur = pre
                return True
            else:
                pre = cur
                cur = cur.next()
        return False

    # remove and return the node at the end of the list, or return None
    def pop(self):
        cur = self.header

        while (cur is not None) and (cur.next is not None):
            cur = cur.next()

        if cur is None:
            return None
        else:
            return cur

    # return the first index of the node in the list if exists, or return -1
    def index(self, node):
        cur = self.header
        i = 0
        while cur is not None:
            if cur.get() == node:
                return i
            # try the next node
            cur = cur.next()
            i += 1
        # not exists
        return -1

    # return whether the node is in the list or not
    def find(self, node):
        cur = self.header
        while cur is not None:
            # compare with value
            if cur.get() == node:
                return True
            cur = cur.next()
        return False

    # represent a node in the list
    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

        # return the value of the Node
        def get(self):
            return self.value

        # set the value of the node
        def set(self, value):
            self.value = value

        # return the next node
        def next(self):
            return self.next

        # set the next node
        def setNext(self, next):
            self.next = next
