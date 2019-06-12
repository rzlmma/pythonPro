# -*- coding:utf-8 -*-
# __author__ = majing

"""
1. 生成最大堆
"""
import random
def max_heapify(alist, i, heap_size):
    lc = 2 * i + 1
    rc = 2 * i + 2

    largest = i
    if lc <= heap_size:
        if alist[lc] > alist[i]:
            largest = lc

    if rc <= heap_size:
        if alist[rc] > alist[largest]:
            largest = rc

    if largest != i:
        alist[i], alist[largest] = alist[largest], alist[i]
        max_heapify(alist, largest, heap_size)


def build_heap(alist):
    n = len(alist)-1
    for i in range(int(n/2)+1, -1, -1):
        max_heapify(alist, i, n)


def heap_sort(alist):
    build_heap(alist)
    size = len(alist)-1
    for i in range(size, 0, -1):
        alist[0], alist[i] = alist[i], alist[0]
        size -= 1
        max_heapify(alist, 0, size)


if __name__ == "__main__":
    alist = random.sample(range(100), 30)
    print("alist: ", alist)
    heap_sort(alist)
    print("after sort: %s" % alist)





