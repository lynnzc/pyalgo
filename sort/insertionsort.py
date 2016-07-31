# !usr/bin/python
# -*- coding: utf-8 -*-


class InsertionSort:

    def __init__(self):
        pass

    # sort a list of datas from min to max
    def sort(self, datas):
        for i in range(1, len(datas)):
            insertData = datas[i]
            for j in range(i, -1, -1):
                # datas in range from [0, i - 1] must be sorted
                if j > 0 and insertData < datas[j - 1]:
                    # swap the data
                    temp = datas[j]
                    datas[j] = datas[j - 1]
                    datas[j - 1] = temp
                else:
                    temp = insertData
                    insertData = datas[j]
                    datas[j] = temp
                    break
        return datas
