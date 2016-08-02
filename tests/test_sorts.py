# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0, '..')

import unittest
import random
from sort.bubblesort import *
from sort.insertionsort import *
from sort.selectionsort import *
from sort.mergesort import *
from sort.quicksort import *


class TestSortsCase(unittest.TestCase):

    def test_selectionsort(self):
        ss = SelectionSort()
        res = ss.sort([2, 3, 5, 2])
        self.assertEqual(res, [2, 2, 3, 5])
        res = ss.sort(self.randomDatas(0, 1000, 20))
        print(res)

    def test_insertionsort(self):
        iss = InsertionSort()
        res = iss.sort([2, 5, 1, 33, 12, 34, 9, 0])
        self.assertEqual(res, [0, 1, 2, 5, 9, 12, 33, 34])
        res = iss.sort(self.randomDatas(0, 1000, 20))
        print(res)

    def test_bubblesort(self):
        bs = BubbleSort()
        res = bs.sort([2, 5, 1, 33, 12, 34, 9, 0])
        self.assertEqual(res, [0, 1, 2, 5, 9, 12, 33, 34])
        res = bs.sort(self.randomDatas(0, 1000, 20))
        print(res)

    def test_mergesort(self):
        ms = MergeSort()
        res = ms.sort([2, 5, 1, 33, 12, 34, 9, 0])
        self.assertEqual(res, [0, 1, 2, 5, 9, 12, 33, 34])
        res = ms.sort(self.randomDatas(0, 1000, 20))
        print(res)

    def test_quicksort(self):
        qs = QuickSort()
        res = qs.sort([2, 5, 1, 33, 12, 34, 9, 0])
        self.assertEqual(res, [0, 1, 2, 5, 9, 12, 33, 34])
        res = qs.sort(self.randomDatas(0, 1000, 20))
        print(res)
        res = qs.qsort(self.randomDatas(0, 1000, 20))
        print(res)

    def randomDatas(self, min, max, size):
        return [random.randint(min, max) for i in range(size)]

if __name__ == "__main__":
    unittest.main()
