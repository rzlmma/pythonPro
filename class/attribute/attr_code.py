# -*- coding:utf-8 -*-
"""
属性代理
   代理是一种编程模式，它将某个操作转移给另一个对象实现
"""

class A:
    def spam(self, x):
        print "A.spam"
        return x**2

    def foo(self, y):
        print "A.foo"
        return y*2


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        print "B.spam"
        return self._a.spam(x)

    def foo(self,y ):
        print "B.foo"
        return self._a.foo(y)


class C:
    def __init__(self):
        self._a = A()

    def __getattr__(self, item):
        return getattr(self._a, item)



#实现代理模式
class Proxy:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, item):
        print "Trace:",item
        return getattr(self.wrapped, item)


class D:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print "D.bar %s %s"%(self.x, y)


class ListLike:
    def __init__(self):
        self._obj = []

    def __getattr__(self, item):
        return getattr(self._obj, item)

if __name__ == '__main__':
    b = B()
    b.spam(3)
    b.foo(3)
    print "--"*8
    c = C()
    print c.spam(3)
    c.foo(3)

    print"--"*8
    d = D(6)
    print "d:",d
    p = Proxy(d)
    p.bar(7)

    print "--"*8
    l = ListLike()
    l.append(5)
    l.append(6)
    print len(l)
    print l[0]