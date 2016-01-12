# -*- coding:utf-8 -*-
"""
python2.x中有新式类和经典类的区别，python3.x中都是新式类
新式类和经典类的区别
(1)类和类型合并
      在新式类中，类实例的类型是派生自的类，而不是instance类型。类是type类型的实例，所有的对象都继承自object
(2)多继承搜索路径的变化
      在经典类中，继承搜索模式从左到右，深度优先
      在新式类中，继承搜索模式从左到右，宽度优先
"""
#经典类
class OldClass:
    data = 'welcome'
    def printf(self):
        print "type(data):",type(OldClass.data)
        print "type(str):",type(str)

#新式类 显示的继承自object或内置类型
class NewClass(object):
    data = 'welcome'
    def printf(self):
        print 'type(data):',type(NewClass.data)
        print "type(str):",type(str)

def show(*args):
    if args[0] == 'oldclass':
        print"==========oldclass======"
    else:
        print "==========newclass======="
    for item in args[1:]:
        print "%s:=========>type:%s"%(item,type(item))



if __name__ == '__main__':
    old = OldClass()
    show('oldclass',old,OldClass)
    old.printf()
    new = NewClass()
    show('newclass',new,NewClass)
    old.printf()