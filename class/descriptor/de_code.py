# -*- coding:utf-8 -*-
"""
属性管理的几种种方法：
1.__getattr__     __getattribute__    __setattr__   __delattr__
2.property
3.描述符

描述符作为一个单独的类对象
def __get__(self, instance, owner)
def __set__(self, instance, value)
def __delete__(self, instance)
"""

class Descriptor(object):
    def __get__(self, instance, owner):
        print"self:{}    instance:{}           owner:{}".format(self, instance, owner)


    #限制基于描述符属性为只读
    def __set__(self, instance, value):
        raise AttributeError('cannot set new attribute')


class A(object):
    data = Descriptor()

if __name__ == '__main__':
    obj = A()
    obj.data
    print "============================="
    A.data

    obj.data = 99