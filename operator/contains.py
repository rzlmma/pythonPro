# -*- coding:utf-8 -*-
"""
in 成员关系测试实现3种方法：__contains__ >(优先)__iter__ > __getitem__
"""
from __future__ import print_function
class MyContains:
    def __init__(self,data):
        self.data = data

    def __getitem__(self, item):
        print("get[%s]:"%(item), end='')
        return self.data[item]

    def __iter__(self):
        print('iter==>',end='')
        self.start = 0
        return self
    def next(self):
        print('next:', end='')
        if self.start >= len(self.data):
            raise StopIteration
        item = self.data[self.start]
        self.start += 1
        return item

    def __contains__(self, item):
        print('contains:',end='')
        return item in self.data

if __name__ == "__main__":
    obj = MyContains([1,2,3,4,5])
    print(4 in obj)

    for i in obj:
        print(i, end='| ')

    print()
    print([i**2 for i in obj])

    print(map(bin, obj))

    I = iter(obj)
    while True:
        try:
            print(I.next(), end=' @ ')
        except StopIteration:
            break

    print()
    print(obj[2:4])