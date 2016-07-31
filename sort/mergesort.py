# !/usr/bin/python
# -*- coding: utf-8 -*-


class MergeSort:

    def __init__(self):
        pass

    # sort a list of datas from min to max
    def sort(self, datas):
        res = []

        if len(datas) < 2:
            # only one element, just return it
            return datas

        mid = len(datas) // 2

        leftSorted = self.sort(datas[:mid])
        rightSorted = self.sort(datas[mid:])

        lI = 0
        rI = 0
        while lI < len(leftSorted) and rI < len(rightSorted):
            if leftSorted[lI] < rightSorted[rI]:
                res.append(leftSorted[lI])
                lI += 1
            else:
                # leftSorted[lI] > rightSorted[rI]
                res.append(rightSorted[rI])
                rI += 1

        res += leftSorted[lI:]
        res += rightSorted[rI:]

        return res
