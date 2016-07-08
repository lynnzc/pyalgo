# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, "..")

from adt.queue import Queue


def testEnqueueQueue(queue, nodes):
    for n in nodes:
        queue.enqueue(n)
    print("queue enqueue ok")


def testPrintQueue(queue):
    print("queue:", end=' ')
    while(queue.size() > 0):
        print(queue.dequeue(), end=' ')
    print("")


def testSizeQueue(queue):
    print("queue size is: ", queue.size())


def testEmptyQueue(queue):
    print("queue is empty: ", queue.isEmpty())

if __name__ == "__main__":
    q = Queue()

    testEnqueueQueue(q, ['1', '2', '3', 4, '5'])

    testSizeQueue(q)

    testPrintQueue(q)

    testEmptyQueue(q)
