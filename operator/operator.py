# -*- coding:utf-8 -*-
"""
运算符重载：
当实例创建的时候，会调用__init__方法
(+,-)  __add__   __sub__
索引 分片     __getitem__
当调用实例的时候，用__call__方法
当实例空间被收回时，会调用__del__方法
定制对象显示  __str__   __repr__
"""
class MyOperator:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return MyOperator(self.value + other)

    def __sub__(self, other):
        return MyOperator(self.value - other)

    def __str__(self):
        return "<MyOperator: %s>" % (str(self.value))   #__str__ should return a string not print

    def __getitem__(self, item):
        print "getitem: item----->%s"%(item)
        return self.value[item]

    def __setitem__(self, key, value):
        print "setitem: value------>%s"%(value)
        self.value[key] = value


class Callback:
    def __call__(self, *args, **kwargs):
        print "args:%s     kwargs:%s" % (args, kwargs)

    def __del__(self):
        print "del the object"

if __name__ == "__main__":
    myobj = MyOperator(5)
    print myobj
    print "---------加法-------"
    print myobj + 8

    print "---------索引 分片------"
    L = [5,6,7,8,9]
    obj = MyOperator(L)
    print obj[4]
    print obj[1:4]

    obj[4] = 89
    print obj.value


    cc = Callback()
    cc(3,4,5,a=7,b=9)
    cc = "goodbye"          #调用析构函数