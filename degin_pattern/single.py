# -*- coding:utf-8 -*-
"""
单例模式
"""
class OnlyOne:
    class __OnlyOne:
        def __init__(self,arg):
            self.value = arg

        def __str__(self):
            return repr(self)+self.value
    instance = None
    def __init__(self,arg):
        if not OnlyOne.instance:
            print "create insatance"
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            print "instance is exists"
            OnlyOne.instance.value = arg

    def __getattr__(self, item):
        return getattr(self,item)

obj = OnlyOne('summnry')
print obj.instance

obj = OnlyOne('happy')
print obj.instance

obj = OnlyOne('new year')
print obj.instance

