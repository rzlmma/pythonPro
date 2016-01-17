# -*- coding:utf-8 -*-
"""
单一实例的类装饰器
"""
class SingleTon:
    def __init__(self, aClass):
        self.aClass = aClass
        self.instance = None

    def __call__(self, *args, **kwargs):
        if self.instance == None:
            self.instance = self.aClass(*args, **kwargs)
        return self.instance

@SingleTon
class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def method(self):
        print "name:%s  job:%s"%(self.name, self.job)


@SingleTon
class Spam:
    def __init__(self,*args):
        self.param = args

    def method(self):
        print "args:",self.param


if __name__ == '__main__':
    bb = Person('Lucy', 'meth')
    bb.method()
    print bb
    print "==========================="
    pp = Person('Samth', 'compute')
    pp.method()
    print "==============================="

    ss= Spam(4,5,6,'welcome')
    ss.method()

    aa = Spam(7,8,9)
    aa.method()

