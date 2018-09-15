# -*- coding:utf-8 -*-
# __author__ = majing
"""
第二章：线性表中的算法实现
"""

"""
2-1：求集合A和集合B的并集
"""

def algorithm_2_1(la, lb):
    i = 0
    while i < len(lb):
        if lb[i] not in la:
            la.append(lb[i])
        i += 1
    return la

"""
2-2: 把两个非递减有序排列的线性表合并成一个非递减有序排列的线性表
有两种想法：1.把B中的数据加入到A中，对新的线性表进行插入排序   最坏情况下的时间复杂度是O(mn)
           2. 分别拿出A，B中的数据，哪个小，就把哪个数据插入到新的线性表中   最坏情况下的时间复杂度是O(mn)
           2比1要好一点
"""

def algorithm_2_2(la,lb):
    la.extend(lb)

    la_count = len(la)
    begin = la_count - len(lb)

    while begin < la_count:
        if la[begin] < la[begin - 1]:
            la[begin], la[begin -1] = la[begin-1], la[begin]
            i = begin - 1

            while i > 0:
                if la[i] < la[i-1]:
                    la[i], la[i-1] = la[i-1], la[i]
                i -= 1
        begin += 1

    return la

def algorithm_2_2_s(la, lb):
    lc = []
    la_count = len(la)
    lb_count = len(lb)

    i, j = 0, 0

    while i < la_count and j < lb_count:
        if la[i] < lb[j]:
            lc.append(la[i])
            i += 1
        else:
            lc.append(lb[j])
            j += 1

    while i < la_count:
        lc.append(la[i])
        i += 1

    while j < lb_count:
        lc.append(lb[j])
        j += 1

    return lc

if __name__ == "__main__":
    la = [i for i in range(1, 1000)]
    lb = [i for i in range(1000, 2000)]

    lc = algorithm_2_2_s(la, lb)

    # lc = algorithm_2_2(la, lb)

