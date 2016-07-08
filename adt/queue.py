# !/usr/bin/python
# coding:utf-8


class Queue:
    def __init__(self):
        self.nodes = []

    # return whether queue is empty or not
    def isEmpty(self):
        return (self.nodes == [])

    # insert a new node to the rear of the queue
    def enqueue(self, node):
        self.nodes.insert(0, node)

    # remove the front node from the queue
    def dequeue(self):
        return self.nodes.pop(0)

    # return the number of nodes in the queue
    def size(self):
        return len(self.nodes)
