# -*- coding:utf-8 -*-
"""
super 调用父类方法
"""
class A(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y
        print "A.__init__"

    def method(self):
        return 2*(self.x + self.y)


class B(A):
    def __init__(self, x,y):
        super(B, self).__init__(x, y)
        print "B.__init__"

    def _method(self):
        r = super(B, self).method()
        return r


class C(A):
    def __init__(self, x, y):
        super(C, self).__init__(x, y)
        print "C.__init__"

    def _method(self):
        r = A.method(self)
        return r

class D(B,C):
    def __init__(self, x, y):
        super(D, self).__init__(x, y)
        print "D.__init__"

if __name__ == '__main__':
    b = B(4,5)
    print b._method()

    c = C(4,5)
    print c._method()

    print"======================="
    d = D(4,5)
    print D.__mro__
