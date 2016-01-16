# -*- coding:utf-8 -*-
"""
类装饰器
"""
instances = {}
def getInstances(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]

def singleTon(aClass):
    def onCall(*args):
        return getInstances(aClass,*args)
    return onCall

@singleTon
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate

@singleTon
class Spam:
    def __init__(self, val):
        self.attr = val

if __name__ == '__main__':
    per = Person('Lucy',23, 1.23)
    print per
    print 'per.name:%s    per.pay:%s'%(per.name, per.pay())
    bob = Person('Bob',45, 2.34)
    print bob
    print 'bob.name:%s    bob.pay:%s'%(bob.name, bob.pay())

    print "============================="
    ss = Spam('welcome')
    print ss.attr

    bb = Spam('to china')
    print bb.attr



