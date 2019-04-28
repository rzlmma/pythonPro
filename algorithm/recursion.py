# -*- coding:utf-8 -*-
# __author__ = majing
"""
递归算法：斐波那契数列
"""


def get_value(n):
    if n == 1:
        return n
    else:
        return n * get_value(n - 1)


def gen_last_value(n, m):
    first = get_value(n)
    second = get_value(m)
    third = get_value((n - m))
    return first / (second * third)


if __name__ == "__main__":
    # C(12,5)
    rest = gen_last_value(6, 3)
    print("value:", rest)
