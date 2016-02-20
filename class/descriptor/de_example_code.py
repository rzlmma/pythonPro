# -*- coding:utf-8 -*-
"""
将描述符类的实例分配给客户类的一个类属性，如果将描述符类实例赋值给self(类实例的)属性，描述符将无法工作
property内置函数仅是创建描述符的一种简便方式
"""


class D(object):
    """
    name descriptor docs
    """
    def __get__(self, instance, owner):
        print "fetch......"
        return instance._name

    def __set__(self, instance, value):
        print "set........."
        instance._name = value

    def __delete__(self, instance):
        print "removing........"
        del instance._name

class A(object):
    name = D()

    def __init__(self, value):
        self._name = value


#用描述符来模拟property内置函数
class Property(object):
    def __init__(self, fget, fset, fdelete, docs):
        self.fget = fget
        self.fset = fset
        self.fdelete = fdelete
        self.__doc__ = docs

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('canot get attribute')
        return self.fget(instance)

    def __set__(self, instance, value):
        if instance is None:
            return self
        if self.fset is None:
            raise AttributeError('cannot set attribute')
        return self.fset(instance, value)

    def __delete__(self, instance):
        if instance is None:
            return self
        if self.fdelete is None:
            raise AttributeError('cannot delete attribute')
        return self.fdelete(instance)

class B(object):
    def __init__(self, name):
        self._name = name

    def fget(self):
        print "get....."
        return self._name

    def fset(self, value):
        print "set......"
        self._name = value

    def fdelete(self):
        print"removing....."
        del self._name

    name = property(fget, fset, fdelete)



if __name__ == '__main__':
    obj = A('Bob')
    print obj.name

    obj.name = 'Samth'
    print obj.name

    print D.__doc__

    print "========================================"

    b = B('Hams')
    print b.name

    b.name = 'robot'
    print b.name
