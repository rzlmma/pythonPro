# -*- coding:utf-8 -*-
# __author__ = majing

"""
1. 生成最大堆
2. 向下搜索
"""


def siftdown(data, begin):
    heap_size = len(data)
    i, j = begin, 2*begin + 1
    value = data[i]

    if j+1 < heap_size:
        heap_max = data[j]
        if data[j] < data[j+1]:
            heap_max = data[j+1]
            j = j+1

        if value < heap_max:
            data[i], data[j] = data[j], data[i]
            i = j
            siftdown(data, i)
    else:
        if j < heap_size:
            if value < data[j]:
                    data[i], data[j] = data[j], data[i]
                    i = j
                    siftdown(data, i)


def build_heap(data):
    end = len(data)
    for i in range(int((end-2)/2), -1, -1):
        siftdown(data, i)

    return data


if __name__ == "__main__":
     data = build_heap([45,34,12,67,3,14,29,78,39, 23,11, 90, 19, 20])
     print("data: %s" % data)




