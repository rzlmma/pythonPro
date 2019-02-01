# -*- coding:utf-8 -*-
# __author__ = majing
"""
和为k的2个数
"""

def sum_k(array, key):
    """
    无序情况下
    """
    rest = []
    i_exsit = []
    for i in range(len(array)):
        if i in i_exsit:
            continue
        if (key-array[i]) in array:
            rest.append((array[i], key-array[i]))
            i_exsit.append(array.index(key-array[i]))
    return rest


def sum_k_sorted(array, key):
    """
    序列有序的情况下 头尾同时遍历，夹逼原则  如果2者之和大于k,则头不动，尾向前移   如果2者之和小于k,则尾不动，头向前移 
    """
    rest = []
    i, j = 0, len(array) - 1
    for p in range(len(array)):
        if i == j:
            break

        if array[i] + array[j] == key:
            rest.append((array[i], array[j]))
            i = i + 1
        elif array[i] + array[j] > key:
            j = j - 1
        else:
            i = i + 1
    return rest

if __name__ == "__main__":
    array = [1,2,9,11,3,6,8,4,7,5,0]
    key = 11

    rest = sum_k(array, key)
    print("[sum_k]rest: ", rest)

    array.sort()
    rest = sum_k_sorted(array, key)
    print("[sum_k_sorted]rest: ", rest)


