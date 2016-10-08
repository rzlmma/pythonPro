# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
原型模式  如果想根据现有的对象复制出一个新的对象，并对其进行修改
"""


class Point(object):
    __slots__ = ["x", "y"]

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point: Point({0}, {1})".format(self.x, self.y)


def make_point(cls, x, y):
    p = cls(x,y)
    print p

if __name__ == "__main__":
    make_point(Point, 5, 6)
    p = Point(1, 6)
    print p.__class__(7, 8)

    # 原型法
    import copy
    p2 = copy.deepcopy(p)
    p2.x = 90
    p2.y = 8
    print p2


