# -*- coding:utf-8 -*-
"""
类装饰器
多层装饰器：
@A
@B
@C
def f():
    pass

f = A(B(C(f)))

"""
def decor(cls):
    class wrapper:
        def __init__(self, *args):
            self.wrapperd = cls(*args)

        def __getattr__(self, item):
            return getattr(self.wrapperd, item)

    return wrapper

class Decor:
    def __init__(self,classobj):
        self.classobj = classobj

    def __call__(self, *args, **kwargs):
        self.wrapper = self.classobj(*args,**kwargs)
        return self

    def __getattr__(self, item):
        return getattr(self.wrapper, item)



@decor
class C:
    attr = 'spam'
    def __init__(self, x, y):
        self.x = x
        self.y = y

@Decor
class D:
    attr = 'spam'
    def __init__(self, x, y):
        self.x = x
        self.y = y

if __name__ == '__main__':
    obj = C(3,5)
    print obj.x
    print obj.y
    print obj.attr

    print "==============="
    dec = D(3,5)
    print obj.x
    print obj.y
    print obj.attr