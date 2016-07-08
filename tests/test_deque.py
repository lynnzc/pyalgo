# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

from adt.deque import Deque


def testEnqueueFrontDeque(deque, nodes):
    print("enqueue front:", end=' ')
    for n in nodes:
        print(n, end=' ')
        deque.enqueueFront(n)
    print("")


def testEnqueueRearDeque(deque, nodes):
    print("enqueue rear:", end=' ')
    for n in nodes:
        print(n, end=' ')
        deque.enqueueRear(n)
    print("")


def testDequeueFrontDeque(deque):
    print("dequeue front: ", deque.dequeueFront())


def testDequeueRearDeque(deque):
    print("dequeue rear: ", deque.dequeueRear())


def testSizeDeque(deque):
    print("deque size is: ", deque.size())


def testIsEmptyDeque(deque):
    print("deque is empty: ", deque.isEmpty())


def testListDeque(deque):
    print("deque: %s" % (deque.__str__()))

if __name__ == "__main__":
    d = Deque()

    testEnqueueFrontDeque(d, [1])
    testEnqueueFrontDeque(d, [2, 3, 4])

    testEnqueueRearDeque(d, [5, 6, 7])

    testSizeDeque(d)
    print("\nbefore dequeue operations")
    testListDeque(d)

    print("\n")
    testDequeueFrontDeque(d)
    testDequeueRearDeque(d)

    print("\nafter dequeue operations")
    testSizeDeque(d)

    testIsEmptyDeque(d)

    testListDeque(d)
