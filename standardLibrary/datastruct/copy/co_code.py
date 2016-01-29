# -*- coding:utf-8 -*-
"""
定制复制行为
"""
import copy
class MyClass:
    def __init__(self, name):
        self.name = name
        # self.age = age

    def __cmp__(self, other):
        return cmp(self.name, other.name)

    def __copy__(self):
        print "__copy__"
        return MyClass(self.name)

    def __deepcopy__(self, memo):
        print "__deepcopy__(): ",memo
        return MyClass(copy.deepcopy(self.name, memo))

if __name__ == '__main__':
    person = MyClass('Bob')
    print "person:",person
    cs = copy.copy(person)
    print "copy:",cs
    ds = copy.deepcopy(person)
    print "deepcopy:",ds
