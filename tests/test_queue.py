# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

from adt.queue import Queue


def testEnqueueQueue(queue, nodes):
    print("enqueue nodes:", end=' ')
    for n in nodes:
        print(n, end=' ')
        queue.enqueue(n)
    print("\nqueue enqueue ok")


def testPrintAllQueue(queue):
    recursivePrintQueue(queue)
    print("")


def recursivePrintQueue(queue):
    if(queue.size() > 0):
        n = queue.dequeue()
        recursivePrintQueue(queue)
        print(n, end=' ')
    else:
        print("queue from first to last:", end=' ')


def testDequeueQueue(queue):
    print("queue dequeue node: ", queue.dequeue())


def testSizeQueue(queue):
    print("queue size is: ", queue.size())


def testEmptyQueue(queue):
    print("queue is empty: ", queue.isEmpty())

if __name__ == "__main__":
    q = Queue()

    testEnqueueQueue(q, ['1', '2', '3', 4, '5'])

    testSizeQueue(q)

    testDequeueQueue(q)

    testPrintAllQueue(q)

    testEmptyQueue(q)
