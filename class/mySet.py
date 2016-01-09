# -*- coding:utf-8 -*-
"""
扩展内置类型
"""
class MySet:
    def __init__(self,value=[]):
        self.data = []
        self.concat(value)

    def intersect(self,value):
        res = []
        for i in value:
            if i in self.data:
                res.append(i)
        return set(res)

    def union(self,value):
        res = self.data[:]
        for i in value:
            if not i in res:
                res.append(i)
        return set(res)

    def concat(self,value):
        for i in value:
            if not i in self.data:
                self.data.append(i)

    def __len__(self): return len(self.data)
    def __getitem__(self, item): return self.data[item]
    def __and__(self, other): return self.intersect(other)
    def __or__(self, other): return self.union(other)
    def __repr__(self): return 'Set:'+ repr(self.data)

if __name__ == '__main__':
    values = [[6,3,9,7,2],set([34,23,1,7,6]),'hello']
    for value in values:
        myset = MySet(value)
        print "myset:",myset
        print "交集：",myset & set([7,6,'e','l'])
        print "并集:",myset | set([7,6,'e','l'])
        print "========================"
