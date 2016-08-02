# !/usr/bin/python
# -*- coding:utf-8 -*-

import random


class QuickSort:

    def __init__(self):
        pass

    def sort(self, datas):
        if len(datas) < 2:
            return datas
        # shuffle
        random.shuffle(datas)
        # sort
        return self.quicksort(datas)

    def quicksort(self, datas):
        if len(datas) < 2:
            return datas

        pivot = self.partition(datas)
        return self.quicksort(datas[:pivot]) + [datas[pivot]] + self.quicksort(datas[pivot + 1:])

    def partition(self, datas):
        sentinel = 0
        index = sentinel

        for i in range(sentinel + 1, len(datas)):
            if datas[i] <= datas[sentinel]:
                index += 1
                datas[i], datas[index] = datas[index], datas[i]

        datas[sentinel], datas[index] = datas[index], datas[sentinel]

        return index

    def qsort(self, datas):
        if len(datas) < 2:
            return datas
        else:
            return self.qsort([i for i in datas[1:] if i < datas[0]]) \
                + [i for i in datas if i == datas[0]] \
                + self.qsort([i for i in datas[1:] if i > datas[0]])
