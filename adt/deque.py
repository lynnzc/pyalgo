# !/usr/bin/pyhon
# -*- coding: utf-8 -*-


class Deque:

    # double-ended queue
    def __init__(self):
        self.nodes = []

    # return whether the deque is empty or not
    def isEmpty(self):
        return (self.nodes == [])

    # return the number of nodes in the dequeue
    def size(self):
        return len(self.nodes)

    # insert a new node to the front of the deque
    def enqueueFront(self, node):
        self.nodes.insert(0, node)

    # insert a new node to the rear of the deque
    def enqueueRear(self, node):
        self.nodes.append(node)

    # remove the node in the front of the deque
    def dequeueFront(self):
        return self.nodes.pop(0)

    # remove the node in the rear of the deque
    def dequeueRear(self):
        return self.nodes.pop()

    def __str__(self):
        return self.nodes
