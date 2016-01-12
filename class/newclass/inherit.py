# -*- coding:utf-8 -*-
class A:
    data = 'search A'
    def __init__(self):
        print "enter A"
        print "exit A"
    def __getattr__(self, item):
        print "A"

class B(A):
    def __init__(self):
        print "enter B"
        A.__init__(self)
        print "exit B"

    # def __getattr__(self, item):
    #     print "B"

class C(A):
    data = 'search C'
    def __init__(self):
        print "enter C"
        A.__init__(self)
        print "exit C"

    def __getattr__(self, item):
        print "C"

class D(B,C):
    def __init__(self):
        print "enter D"
        B.__init__(self)
        C.__init__(self)
        print "exit D"
    # def __getattr__(self, item):
    #     print "D"

class F(object):
    data = 'search F'
    def __init__(self):
        print "enter F"
        print "exit F"

class G(F):
    def __init__(self):
        print"enter G"
        F.__init__(self)
        print "exit G"

class H(F):
    data = 'search H'
    def __init__(self):
        print"enter H"
        F.__init__(self)
        print "exit H"

class K(G,H):
    def __init__(self):
        print "enter K"
        G.__init__(self)
        H.__init__(self)
        print "exit K"

if __name__ == "__main__":
    d = D()
    print d.name
    print "=="*20
    k = K()
    print k.data