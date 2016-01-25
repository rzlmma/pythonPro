# -*- coding:utf-8 -*-
"""
几种常见的排序算法
"""

#冒泡排序
def sort_mp(value):
    n = len(value)
    for i in range(n-1):
        for j in range(n-1-i):
            if value[j] > value[j+1]:
                temp = value[j+1]
                value[j+1] = value[j]
                value[j] = temp
    return value

if __name__ == '__main__':
    value = [67,12,9,56,27,19,1,34,62]
    print sort_mp(value)
