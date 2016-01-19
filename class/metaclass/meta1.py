# -*- coding:utf-8 -*-
"""
元类
"""
class MetaOne(type):
    def __new__(meta, classname, supers, attributedicts):
        print "in MetaOne ====>   meta:%s  classname:%s  supers:%s   attributedicts:%s"%(meta, classname, supers, attributedicts)
        return type.__new__(meta, classname, supers, attributedicts)

class Eggs(object):
    pass

class Spams(Eggs):
    print "create Spams"
    __metaclass__ = MetaOne
    data = 1
    def meth(self):
        print "in spams"

if __name__ == '__main__':
    ss = Spams()
    ss.meth()