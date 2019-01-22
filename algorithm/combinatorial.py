# -*- coding:utf-8 -*-
# __author__ = majing
"""
求给定序列所有的组合
"""

import copy


def bottom(val):
    if len(val) == 1:
        return val

    return [[val[0]], [val[1]], val[0:2]]


def combinatorial(val):
    rest = bottom(val)

    b_rest = copy.deepcopy(rest)

    for i in range(2,len(val)):
        for item in b_rest:
            n_item = copy.deepcopy(item)
            n_item.append(val[i])
            rest.append(n_item)
        rest.append([val[i]])
        b_rest = copy.deepcopy(rest)

    return rest

if __name__ == "__main__":

    aa = combinatorial(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    print("aa after: ", aa)
    print("len(aa): ", len(aa))



