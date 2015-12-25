# -*- coding:utf-8 -*-
"""  打印出1-100之间的偶数
"""
from __future__ import print_function
import time

# for loop
def forLoop():
    for i in xrange(1,101):
        if i%2 == 0:
            print(i,end=',')

#列表解析
def func():
    item = [i for i in xrange(1,101) if i%2 == 0]
    print (item)


#map
def mapFunc():
    item = filter(lambda i: i%2== 0,range(1,101))
    print(item)

#生成器
def generate():
    for i in (item for item in range(101) if item%2 == 0):
        print (i,end=',')

#计算耗时函数
def timeCost(func):
    print ("<function name:%s>"%(func.__name__))
    start = time.clock()
    func()
    timecost = time.clock() - start
    print(timecost)

if __name__ == "__main__":
    print("timecost:------------------------------")
    for item in [forLoop,func,mapFunc,generate]:
        timeCost(item)
