# -*- coding:utf-8 -*-
class tracer:
    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args, **kwargs):
        self.wrapped = self.aClass(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print "trace:%s"%(item)
        return getattr(self.wrapped, item)

@tracer
class Person:
    def __init__(self, name):
        self.name = name

@tracer
class Spam:
    def __init__(self, value):
        self.value = value

if __name__ == '__main__':
    bob = Person('Bob')
    print bob.name
    sue = Person('Sue')
    print sue.name
    print 'Bob: name====>%s'%(bob.name)       #最后一次产生的实例覆盖了前面一次产生的实例
