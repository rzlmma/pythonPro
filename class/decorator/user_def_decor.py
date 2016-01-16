# -*- coding:utf-8 -*-
"""
用户自定义的装饰器
"""
class Tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print "func name:%s  calls:%s" %(self.func.__name__,self.calls)
        self.func(*args, **kwargs)


def tracer(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print "calls %s to %s"%(wrapper.calls, func.__name__)
        return func(*args,**kwargs)
    wrapper.calls = 0
    return wrapper


@tracer
class A:
    def __init__(self,*args, **kwargs):
        pass
    def method(self, *args, **kwargs):
        print "args:",args
        print "kwrags:",kwargs

@Tracer            #spam = Tracer(spam)
def spam(a,b,c):
    print a,b,c

@Tracer
def test(a,b,c,name=None,age=None):
    print a,b,c
    print 'name:',name
    print 'age:',age

@tracer
def funcs(a,b,c):
    print (a+b+c)

@tracer
def eggs(a,b):
    print (a**b)

if __name__ == '__main__':
    values = [('welcome','to','china'),(2,3,4), (7,8,9)]
    for item in values:
        spam(*item)
        print "spam.calls:",spam.calls
        print "====================="

    test(1,2,3,name='Bob',age=89)

    for item in values:
        funcs(*item)
        print "======================"

    for item in [(5,6),(8,9)]:
        eggs(*item)
        print "==========================="

    aa = A(3,4,5,'welcome to china')
    aa.method(3,4,5,'welcome to china')
    print "============================"
    bb = A(6,7,a='success',b='test')
    bb.method(6,7,a='success',b='test')