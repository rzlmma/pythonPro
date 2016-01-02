# -*- coding:utf-8 -*-
"""
python_version = 2.7
用户定义的迭代器
重载__iter__(),next()方法，python3.0重载__next__()
"""
from __future__ import print_function
#单迭代器
class MyIter:
    def __init__(self,start,stop):
        self.start = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def next(self):
        if self.start == self.stop:
            raise StopIteration
        self.start += 1
        return self.start **2

#创建多迭代器
class MyIterator:
    def __init__(self,value):
        self.value = value
        self.offest = 0

    def next(self):
        if self.offest >= len(self.value):
            raise StopIteration
        item = self.value[self.offest]
        self.offest += 2
        return item

class SkiperObject:
      def __init__(self,vlaue):
          self.value = vlaue

      def __iter__(self):
          return MyIterator(self.value)

if __name__ == "__main__":
    for item in MyIter(1,5):
        print(item,end=',')

    print()
    obj = SkiperObject('abcdef')
    for x in obj:
        for y in obj:
            print(x+y, end=' ')