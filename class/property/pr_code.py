# -*- coding:utf-8 -*-
"""
python2.x 新式类和 python3
"""

class Person(object):
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch....')
        return self._name

    def setName(self, value):
        print('set...')
        self._name = value

    def delName(self):
        print('delete....')
        del self._name

    name = property(getName, setName, delName, 'name attribute property docs')


#特性是可继承的
class Teacher(Person):
    def showInfo(self):
        print self.name
        self.name = "Joes"
        print self.name


#计算属性
class ProSquar(object):
    def __init__(self, x):
        self.x = x

    def getX(self):
        return self.x ** 2

    def setX(self, value):
        self.x = value

    data = property(getX, setX)


#装饰器写法
class People(object):
    def __init__(self, name):
        self._name = name

    @property
    def first_name(self):
        print "fetch attribute..."
        return self._name

    @first_name.setter
    def first_name(self, value):
        print "set attribute..."
        if not isinstance(value, str):
            raise TypeError('need a string')
        self._name = value

    @first_name.deleter
    def first_name(self):
        print"remove attribute..."
        raise AttributeError('cannot delete the attribute')

if __name__ == '__main__':
    p = Person('Bob')
    print p.name
    p.name = 'Sam'
    print p.name
    print Person.name.__doc__

    print '====='*6
    t = Teacher('Smith')
    t.showInfo()

    print '========================'
    p = ProSquar(4)
    print p.data
    p.data = 6
    print p.data

    print "==============================="
    pp = People("Spam")
    print pp.first_name
    pp.first_name = "Jhon"
    print pp.first_name

    del pp.first_name