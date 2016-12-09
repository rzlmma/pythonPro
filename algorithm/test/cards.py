# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
随机生成13张纸牌  a,b,c,d 表示4类牌
"""
import random


def gen_cards():
    total_cards = []
    for item in ["a", "b", "c", "d"]:
        for n in range(1,14):
            card = {}
            card[item] = n
            total_cards.append(card)
    return random.sample(total_cards, 13)


if __name__ == "__main__":
    card = gen_cards()
    print "card:", card





