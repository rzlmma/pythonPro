# -*- coding:utf-8 -*-
"""
分治法 排序
思想：
    两个子数组都排好序，然后合并两个已排序的子数组
   合并的思想是：依次取出两个数组中的最小的元素
"""
import random

def merge(alist, p, q, r):
    left_list = alist[p:q+1]
    right_list = alist[q+1:r+1]
    left_list.append(float("inf"))
    right_list.append(float("inf"))
    i = j = 0
    for k in range(p, r+1):
        if left_list[i] <= right_list[j]:
            alist[k] = left_list[i]
            i = i+1
        else:
            alist[k] = right_list[j]
            j = j+1


def merge_sort(alist, p, r):
    if p < r:
        q = (p+r)/2
        merge_sort(alist, p, q)
        merge_sort(alist, q+1, r)
        merge(alist, p, q, r)

if __name__ == "__main__":
    alist = random.sample(range(1, 100), 19)
    print("befor sort:", alist)
    merge_sort(alist,0,18)
    print("after sort:", alist)
