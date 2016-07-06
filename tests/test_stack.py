#!/usr/bin/python
# coding:utf-8
import sys
sys.path.insert(0, '..')

from adt.stack import Stack

# test for Stack
if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)

    print(s)
    print(s.peek())

    s.pop()

    print(s)

    print(s.size())
