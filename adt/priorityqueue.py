# !/usr/bin/python
# -*- coding: utf-8 -*-


class PriorityQueue:
    # binary max heap implement
    def __init__(self):
        self.heap = [0]
        self.size = 0

    # insert a new node to the priority queue
    def insert(self, key):
        self.heap.append(key)
        self.size += 1
        self.swim(self.size)

    # return the max key node from the priority queue
    def max(self):
        if self.size == 0:
            return None
        return self.heap[1]

    # pop the max key node from the priority queue
    def popMax(self):
        if self.size == 0:
            return None
        maxKey = self.heap[1]
        self.heap[1] = self.heap[self.size]
        # remove the last node
        self.heap.pop()
        self.size -= 1
        self.sink(1)
        return maxKey

    # return whether the priority queue is empty or not
    def isEmpty(self):
        return (self.size == 0)

    # return the number of nodes in priority queue
    def count(self):
        return self.size

    def __str__(self):
        return self.heap

    def swim(self, i):
        while i // 2 > 0:
            if self.heap[i // 2] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i // 2]
                self.heap[i // 2] = temp
            i //= 2

    def sink(self, i):
        while i * 2 <= self.size:
            child = 2 * i
            if child < self.size and self.heap[child] < self.heap[child + 1]:
                child += 1
            if self.heap[child] > self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[child]
                self.heap[child] = temp
            i = child

    # create a heap from a list
    def buildHeap(self, listToHeap):
        startIndex = len(listToHeap) // 2
        self.size = len(listToHeap)
        self.heap = [0] + listToHeap
        while startIndex > 0:
            self.sink(startIndex)
            startIndex -= 1
