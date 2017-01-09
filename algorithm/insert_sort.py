# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack

"""
插入排序
"""


def sort_acm(sort_list):
    """
    升序
    """
    for j in range(1, len(sort_list)):
        key = sort_list[j]
        i = j - 1
        while i >= 0 and sort_list[i] > key:
            sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
            i -= 1
    print "sorted list:", sort_list


def sort_desc(sort_list):
    """
    降序
    """
    for j in range(1, len(sort_list)):
        key = sort_list[j]
        i = j - 1
        while i >= 0 and sort_list[i] < key:
            sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
            i -= 1
    print "sorted list:", sort_list


if __name__ == "__main__":
    sort_list = [5, 2, 6, 9, 1, 7, 3]
    sort_acm(sort_list)
    sort_desc(sort_list)

