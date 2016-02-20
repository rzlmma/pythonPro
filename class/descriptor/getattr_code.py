# -*- coding:utf-8 -*-
"""
__getattr__     未定义的属性
__getattribute__         访问所有的属性

__setattr__避免递归的两种方式：
def __setattr__(self, name, value):
    self.__dict__[name] = value

def __setattr__(self, name, value):
    object.__setattr__(self, name, value)

def __getattribute__(self, name):
    x = object.__getattribute__(self, name)
"""
class GetAttr:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print "__len__:42"
        return 42

    def __getattr__(self, item):
        print"gettattr:" + item
        if item == '__str__':
            return lambda *args: '[Getattr str]'
        else:
            return lambda *args: None


class Getattribute(object):
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print "__len__: 42"
        return 42

    def __getattribute__(self, item):
        print "getattribute:"+item
        if item == '__str__':
            return lambda *args: '[Getattribute: str]'
        else:
            return lambda *args: None

if __name__ == '__main__':
    for item in [GetAttr, Getattribute]:
        print item.__name__.center(40, '=')
        obj = item()
        obj.eggs
        obj.spam
        obj.other()
        len(obj)

        try:
            obj[0]
        except:
            print 'fail: []'


        try:
            obj + 99
        except:
            print 'fail +'

        try:
            obj()
        except:
            print "fial ()"

        obj.__call__()

        print obj.__str__()
        print obj


