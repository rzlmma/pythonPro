# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
""""
    比较冒泡排序和python内置的sort排序时间
"""

import time


def show_time(func):
    def _wrapper(*args, **kwargs):
        start_time = time.clock()
        rest = func(*args, **kwargs)
        cost_time = time.clock() - start_time
        print u"函数名：%s          运行时间:%s"%(func.__name__, cost_time)
    return _wrapper


@show_time
def python_sort(param):
    param.sort()
    print u"排序后的序列:%s" % param


@show_time
def my_sort(param):
    length = len(param) - 1
    for i in range(length):
        for j in range(0, length-i):
            if param[j] >= param[j+1]:
                temp = param[j]
                param[j] = param[j+1]
                param[j+1] = temp
    print u"排序后的序列:%s"%param


@show_time
def insert_sort(param):
    """
    插入排序
    """
    new_list = []
    first_number = param.pop(0)
    new_list.append(first_number)
    for i in range(0, len(param)):
        for j in range(len(new_list)-1, -1, -1):
            if param[i] >= new_list[j]:
                new_list.insert(j+1, param[i])
                break
            if j == 0:
                new_list.insert(0, param[i])

    print u"排序后的序列:%s" % new_list


if __name__ == "__main__":
    sort_list = [45,3,78,12,20,6,67,29,13,90]
    python_sort(sort_list)

    sort_list = [45, 3, 78, 12, 20, 6, 67, 29, 13, 90]
    my_sort(sort_list)

    sort_list = [45, 3, 78, 12, 20, 6, 67, 29, 13, 90]
    insert_sort(sort_list)



