# -*- coding:utf-8 -*-
"""
itertools
"""
from __future__ import print_function
from itertools import *
import operator

def chain_zip():
    #把多个序列合并成一个迭代器
    print('chain:')
    for item in chain([3,4,5,6],"happy"):
        print(item, end=' ')

    print()

    #把多个迭代器的元素合并在元组中
    print('izip:')
    for item in izip([3,4,5,6],('a','b','c')):
        print(item, end=' ')

    print()

    for item in izip([3,4,5,6],('a','b','c','d')):
        print(item, end=' ')

def it_islice():
    print('islice:')
    value = [4,5,6,7,8,9,12,13,45,67,89,33,23]
    for item in islice(value,4):
        print(item, end=' ')
    print()
    for item in islice(value, 2,8):
        print(item, end=' ')
    print()
    for item in islice(value, 0,8,3):
        print(item, end=' ')

    print()
    r = islice(value, 2,8)
    it, ir = tee(r)
    print('it:%s'%(list(it)))
    print('ir:%s'%(list(ir)))

def it_imap():
    print("imap:")
    for item in imap(lambda x: x**2, range(5)):
        print(item,end=' ')

    print()

    for item in imap(lambda x,y: (x,y, x*y), range(5), range(5,12)):
        print("x:%s   y:%s  x*y:%s"%item)

def it_repeat():
    for i,item in izip(count(3), repeat('happy new yeay',5)):
        print("%s: %s"%(i,item))

    for item in imap(lambda x,y: (x,y, x*y), xrange(5),repeat(2)):
        print("%d * %d = %d"%item)

def it_dropwhile():
    value = [3,4,5,-2,7,8,9]
    for item in dropwhile(lambda x: x>0, value):
        print(item, end=' ')

    print()
    for item in takewhile(lambda x:x>0, value):
        print(item, end=' ')

#groupby
class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return '(%s, %s)'%(self.x, self.y)

    def __cmp__(self, other):
        return cmp((self.x, self.y), (other.x, other.y))

if __name__ == '__main__':
    it_imap()
    print()
    it_repeat()
    print('dropwhile:')
    it_dropwhile()
    print()
    print('==============================')
    print('datas unsorted:')
    datas = list(imap(Point, cycle(islice(count(),3)), xrange(7)))
    for i,k in groupby(datas,operator.attrgetter('x')):
        print("i:%s  k:%s"%(i,list(k)))

    print('datas sorted:')
    datas.sort()
    print('datas:{}'.format(datas))
    for i,j in groupby(datas,operator.attrgetter('x')):
        print("i:%s  k:%s"%(i,list(j)))
