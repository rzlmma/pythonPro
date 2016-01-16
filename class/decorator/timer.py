# -*- coding:utf-8 -*-
"""
计算调用时间的装饰器
"""
import time
class Timer:
    def __init__(self, funcs):
        self.alltime = 0
        self.func = funcs

    def __call__(self, *args, **kwargs):
        start = time.clock()
        result = self.func(*args, **kwargs)
        timecost = time.clock() - start
        self.alltime += timecost
        print "<function>%s cost %.5f,total time is %.5f"%(self.func.__name__, timecost, self.alltime)
        return self.func(*args, **kwargs)

#带参数的装饰器
def timer_param(lable, trace=True):
    class TimeCost:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args, **kwargs):
            start = time.clock()
            rest = self.func(*args, **kwargs)
            time_cost = time.clock() - start
            self.alltime += time_cost
            print "<function> %s %s cost %.5f, total time is %.5f"%(lable, self.func.__name__, time_cost, self.alltime)
            return rest
    return TimeCost

@Timer
def listloop(N):
    return [item *2 for item in range(N)]

@Timer
def maploop(N):
    return map(lambda x:x*2 , range(N))

@timer_param('=====>')
def func1(N):
    return [item *2 for item in range(N)]

@timer_param('======>')
def func2(N):
    return map(lambda x:x*2 , range(N))

if __name__ == '__main__':
    for i in [5,500,5000,50000]:
        listloop(i)
        maploop(i)
        func1(i)
        func2(i)
        print "======================="
