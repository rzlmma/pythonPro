# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
行程长度压缩算法：
    将序列中的相同的部分表示为数量，原始字符的模式；没有重复的部分表示为1，原始字符的模式
    "getaaaabbaa"    1g1e1t4a2b2a
"""


def my_rle(sequeue):
    length = len(sequeue)
    rest = []
    temp = 0
    for index, value in enumerate(sequeue):
        count = 1
        if temp != index:
            continue
        if temp + 1 < length:
            if value != sequeue[temp + 1]:
                rest.append([value, count])
                temp += 1
            else:
                if temp + 1 < length:
                    while sequeue[temp] == value:
                        count += 1
                        temp += 1
                        if temp == length:
                            break
                    rest.append([value, count])
    return rest


if __name__ == "__main__":
    old_list = "getaaaaaaaupbbbbbbbbbbbbaaaaaaaaaa"
    ss = my_rle(old_list)
    print "ss:", ss

