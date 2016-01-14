# -*- coding:utf-8 -*-
"""
修改可变的类属性会影响其他的实例
嵌套作用域
"""
class A:
    data = 1
    shared = []
    def __init__(self):
        self.perobj = []


def generate():
    class Spam:
        count = 10
        def method(self):
            print Spam.count
    return Spam()

if __name__ == '__main__':
    x = A()
    y = A()
    print "x.data:",x.data
    print "x.shared:", x.shared

    print "y.data:", y.data
    print "y.shared:",y.shared
    print"============================="

    x.data = 23              #给实例x增加了属性data，并不是改变A中的data的值
    print "x.data:",x.data
    print "y.data:",y.data
    print "A.data:",A.data

    print "====================="
    x.shared.append('welcome')
    x.perobj.append('welcome')
    print 'x.shared:',x.shared
    print 'y.shared:',y.shared
    print 'A.shared:',y.shared

    print "================"
    generate().method()