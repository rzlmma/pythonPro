# -*- coding:utf-8 -*-
"""
在函数被调用时打印耗时详情
"""
import time

def hello(name):
    print "hello,%s"%name

def printInfo(func):
    print "<function name:%s>"%(func.__name__)
    print "<fuction call begin>"
    start = time.clock()
    hello('tom')
    print "<function call end>"
    timecosts = time.clock() - start
    print "[timecosts:%s]"%(timecosts)

if __name__ == "__main__":
    printInfo(hello)
