# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
"""
队列  先进先出
"""


class Queue(object):
    def __init__(self, max_size=float('inf')):
        self._max_size = max_size
        self._top = 0
        self._tail = 0
        self._queue = []

    def put(self, value):
        if self.isFull():
            raise ValueError("the queue is full")
        self._queue.insert(self._tail, value)
        self._tail += 1

    def pop(self):
        if self.isEmpty():
            raise ValueError("the queue is empty")
        data = self._queue.pop(self._top)
        self._top += 1
        return data

    def isEmpty(self):
        if self._top == self._tail:
            return True
        else:
            return False

    def isFull(self):
        if self._tail == self._max_size:
            return True
        else:
            return False

    def __str__(self):
        return "Queue(%s)"%self._queue


if __name__ == "__main__":
    q = Queue(10)
    q.put(1)
    q.put(2)
    q.put('hell world')
    q.put([3,4,5])
    print "Queue:", q
    print "****************"
    print q.pop()
    print q.pop()