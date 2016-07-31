# !usr/bin/python
# -*- coding: utf-8 -*-


class SelectionSort:

    def __init__(self):
        pass

    # sort a list of datas from min to max
    def sort(self, datas):
        for i in range(len(datas)):
            minIndex = i
            for j in range(i + 1, len(datas)):
                if datas[minIndex] > datas[j]:
                    minIndex = j
            if i != minIndex:
                temp = datas[i]
                datas[i] = datas[minIndex]
                datas[minIndex] = temp

        return datas
