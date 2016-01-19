# -*- coding:utf-8 -*-
"""
元类重载类创建调用
"""
class SuperMeta(type):
    print "In SuperMeta....."
    def __call__(meta, classname, supers,attributedicts):
        print "meta:%s\n classname:%s\n supers:%s\n attributedicts:%s\n"%(meta,classname,supers,attributedicts)
        return type.__call__(meta,classname,supers,attributedicts)


class SubMeta(type):
    __metaclass__ = SuperMeta
    def __new__(meta, classname, supers,attributedicts):
        print "In SubMeta....."
        print "meta:%s\n classname:%s\n supers:%s\n attributedicts:%s\n"%(meta,classname,supers,attributedicts)
        return type.__new__(meta, classname, supers,attributedicts)

    def __init__(meta, classname, supers,attributedicts):
        print "Init ...."
        print "meta:%s\n classname:%s\n supers:%s\n attributedicts:%s\n"%(meta,classname,supers,attributedicts)


class Eggs(object):
    pass


class Spams(Eggs):
    __metaclass__ = SubMeta
    data = 1
    def meth(self):
        pass

if __name__ == '__main__':
    X = Spams()
    print X.data