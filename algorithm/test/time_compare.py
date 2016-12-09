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
        for j in range(i, length):
            if param[j] > param[j+1]:
                temp = param[j]
                param[j] = param[j+1]
                param[j+1] = temp
    print u"排序后的序列:%s"%param

if __name__ == "__main__":
    sort_list = [45,3,78,12,20,6,67,29,13,90]

    python_sort(sort_list)
    my_sort(sort_list)



