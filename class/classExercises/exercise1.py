# -*- coding:utf-8 -*-
"""
list是序列的一种,所以它支持+，*操作
字符串拼接用join方法比较快
list拼接用extend方法比较快
"""
class Adder:
    def __init__(self, obj=[]):
        self.data = obj

    def __add__(self, other):
        if isinstance(self.data, dict):
            rest = {}
            if self.data:
                for key,value in self.data.items():
                    rest[key] = value
            rest.update(other)
            return rest
        else:
            rest = self.data[:]
            rest.extend(other)
            return rest

    def add(self,x,y):
        print "Not Implemented"

class ListAdder(Adder):
    def __init__(self, obj=[]):
        Adder.__init__(self,obj)

    def add(self,x,y):
        return x+y

class DictAdder(Adder):
    def __init__(self, obj={}):
        Adder.__init__(self, obj)

    def add(self,x,y):
        x.update(y)
        return x


if __name__ == "__main__":
    for item in [Adder, ListAdder, DictAdder]:
        obj = item()
        print "class name:", item.__name__
        if isinstance(obj.data, dict):
            print obj + {'name':'Lucy','age':34}
            print"obj.add:", obj.add({'1':'red', '2':'yellow'}, {'3':'blue'})
        else:
            print obj + [4,5,6,7,8]
            print "obj.add:",obj.add(56,78)
        print "===================="
