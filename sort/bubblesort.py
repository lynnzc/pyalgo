# !/usr/bin/python
# -*- coding: utf-8 -*-


class BubbleSort:

    def __init__(self):
        pass

    # sort a list of datas from min to max
    def sort(self, datas):
        for i in range(len(datas)):
            for j in range(len(datas) - 1, i - 1, -1):
                if j > 0 and datas[j] < datas[j - 1]:
                    temp = datas[j - 1]
                    datas[j - 1] = datas[j]
                    datas[j] = temp
        return datas
