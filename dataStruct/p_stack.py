# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
栈     先进后出
python 实现栈
"""


class Stack(object):
    def __init__(self):
        self._top = 0
        self._stack = []

    def put(self, data):
        self._stack.insert(self._top, data)
        self._top += 1

    def pop(self):
        if self.isEmpty():
            raise ValueError('stack 为空')
        self._top -= 1
        data = self._stack[self._top]

        return data

    def isEmpty(self):
        if self._top == 0:
            return True
        else:
            return False

    def __str__(self):
        return "Stack(%s)"%self._stack


if __name__ == "__main__":
    s = Stack()
    s.put(1)
    s.put(2)
    s.put([5,6,7])
    print s
    print "**************************"
    print s.pop()
