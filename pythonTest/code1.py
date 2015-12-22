# -*- coding:utf-8 -*-
"""  打印出1-1亿之间的偶数
"""
from __future__ import print_function
import time

# for loop
def forLoop():
    start = time.clock()
    for i in xrange(1,100000001):
        if i%2 == 0:
            print(i,end=',')
    res = time.clock()-start
    return res

#列表解析
def func():
    start = time.clock()
    item = [i for i in xrange(1,100000001) if i%2 == 0]
    print (item)
    res = time.clock() - start
    return res

#map
def mapFunc():
    start = time.clock()
    item = filter(lambda i: i%2== 0,range(1,100000001))
    print(item)
    res = time.clock()-start
    return res

if __name__ == "__main__":
    forLoop()
    print("----"*6)
    func()
    print("----"*6)
    mapFunc()