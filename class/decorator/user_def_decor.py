# -*- coding:utf-8 -*-
class Tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print "func name:%s  calls:%s" %(self.func.__name__,self.calls)
        self.func(*args, **kwargs)

@Tracer
def spam(a,b,c):
    print a,b,c

if __name__ == '__main__':
    spam('welcome','to','china')

