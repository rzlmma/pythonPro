# -*- coding:utf-8 -*-
import random

def quick_sort(alist, begin, end):
    if begin < end:
        q = partition(alist, begin, end)
        quick_sort(alist, begin, q-1)
        quick_sort(alist, q+1, end)


def partition(alist, begin, end):
    i = begin - 1
    x = alist[end]

    for j in range(begin, end):
        if alist[j] < x:
            i += 1
            alist[j], alist[i] = alist[i], alist[j]


    alist[i+1], alist[end] = alist[end], alist[i+1]

    return i+1


if __name__ == "__main__":
    aa = random.sample(range(0, 50), 20)
    quick_sort(aa, 0, 19)
    print("after aa: ", aa)