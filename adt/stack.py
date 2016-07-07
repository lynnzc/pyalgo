# !/usr/bin/python
# coding:utf-8


class Stack:

    def __init__(self):
        self.nodes = []

    # check whether stack is empty or not
    def isEmpty(self):
        return (self.nodes == [])

    # remove the element on top of the stack
    def pop(self):
        return self.nodes.pop()

    # insert a new element at the top of the stack
    def push(self, node):
        self.nodes.append(node)

    # return the top node of stack
    def peek(self):
        return self.nodes[self.size() - 1]

    # return the number of nodes in the stack
    def size(self):
        return len(self.nodes)
