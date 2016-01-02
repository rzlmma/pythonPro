# -*- coding:utf-8 -*-
"""
运算符重载(+,-) 索引 分片
"""
class MyOperator:
    def __init__(self,value):
        self.value = value

    def __add__(self, other):
        return MyOperator(self.value + other)

    def __sub__(self, other):
        return MyOperator(self.value - other)

    def __str__(self):
        return "<MyOperator: %s>" % (str(self.value))   #__str__() should return a string not print

    def __getitem__(self, item):
        print "getitem: item----->%s"%(item)
        return self.value[item]

    def __setitem__(self, key, value):
        print "setitem: value------>%s"%(value)
        self.value[key] = value


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
