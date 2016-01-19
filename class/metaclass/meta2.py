# -*- coding:utf-8 -*-
"""
简单工厂函数
"""
def MetaFunc(classname, supers, classdicts):
    print "In MetaFunc......."
    print "classname:%s\n   supers:%s\n    classdicts:%s"%(classname, supers, classdicts)
    return type(classname,supers, classdicts)

class Eggs(object):
    pass

print "create Spam....."
class Spam(Eggs):
    __metaclass__ = MetaFunc
    data = 1
    def meth(self):
        pass

print "create instance......"

if __name__ == '__main__':
    X = Spam()
    print X.data
