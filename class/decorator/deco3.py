# -*- coding:utf-8 -*-
"""
类装饰器
"""
def tracer(aClass):
    class Wrapper:
        def __init__(self,*args, **kwargs):
            self.fetchall = 0
            self.wrapped = aClass(*args, **kwargs)

        def __getattr__(self, item):
            print "trace:%s"%(item)
            self.fetchall += 1
            return getattr(self.wrapped, item)
    return Wrapper

@tracer
class Person:
    def __init__(self, name, hours,rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        print "pay:",self.hours * self.rate

@tracer
class Spam:
    def paly(self):
        print "Spam"*8

if __name__ == '__main__':
    bb = Person('Bob', 43, 1.23)
    print "name:%s  hours:%s  rate:%s"%(bb.name, bb.hours, bb.rate)
    bb.pay()
    print bb
    print bb.__dict__
    print "dir(bb):",dir(bb)
    print "==============================="
    sue = Person('Sue',23, 4.5)
    print "name:%s  hours:%s  rate:%s"%(sue.name, sue.hours, sue.rate)
    sue.pay()
    print "==========================="
    print "name:%s  hours:%s  rate:%s"%(bb.name, bb.hours, bb.rate)

    print '============================'
    ss = Spam()
    print ss.paly()
