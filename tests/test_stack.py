# !/usr/bin/python
# coding:utf-8

import sys
sys.path.insert(0, '..')

from adt.stack import Stack


def testPrintStack(stack):
    recurPrintStack(stack)
    print("")


def recurPrintStack(stack):
    if (stack.size() == 0):
        print("stack: ", end=" ")
    elif(stack.size() > 0):
        i = stack.pop()
        recurPrintStack(stack)
        print(i, end=" ")


def testPushStack(stack, nodes):
    for n in nodes:
        stack.push(n)


def testSizeStack(stack):
    print("stack size is: ", stack.size())


def testEmptyStack(stack):
    print("stack is empty: ", stack.isEmpty())

# test for Stack
if __name__ == "__main__":
    s = Stack()

    testPushStack(s, [1, 2, 3, 4, 5])
    testPrintStack(s)
    testPushStack(s, [12, 13])

    testEmptyStack(s)

    testPrintStack(s)
    testPushStack(s, [22, 33])

    testSizeStack(s)
