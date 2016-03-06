# -*- coding:utf-8 -*-
"""
共享变量
"""
from threading import *
a = b = c = d = 50
def print_vars():
    print "a= ",a
    print 'b= ',b
    print 'c= ',c
    print 'd= ',d

def thread_code(n):
    global a,b,c,d
    a += 50
    b = b+ 50
    c = 100
    if n == '1':
        d = 'hello'
    else:
        d = 'happy'
    print "[ChildThread] values of varibales in ChildThread:"
    print_vars()

print "[MainThread] values of varibales in MainThread:"
print_vars()

t = Thread(target=thread_code,args=('1',), name='ChildThread')
w = Thread(target=thread_code, args=('2',), name='testThread')
t.start()
w.start()

t.join()
t.join()
print "[MainThread] after ChildThread"
print_vars()

a = 200
print "[MainThread] change the a:"
print_vars()
