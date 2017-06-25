# -*- coding:utf-8 -*-
# 迭代队象：可以在迭代工具环境下一次返回一个值得对象都是可迭代的   迭代对象要实现__iter__方法
# 迭代器：实现__iter__   next()方法 文件对象是自身的迭代器 dictionary也实现了一些迭代器, 内置的迭代器 iter, ditc.iteritems, iterkekys, itervalues


#  自定义迭代器
class MyIter(object):
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def next(self):
        if isinstance(self.obj, (list, tuple, str)):
            count = 0
            if count < len(self.obj):
                value = self.obj[count]
                count += 1
            else:
                raise StopIteration()
            return value
        else:
            raise TypeError(u'这里需要一个可迭代的对象')

# 自定义可迭代对象
class Myiterobj(object):
    def __init__(self, value):
         self.value = value

    def __iter__(self):
        print "call __iter__ function"
        return iter(self.value)


if __name__ == "__main__":
    ll = [2,3,4,5,6,7,7]
    new_ll = MyIter(ll)
    print new_ll.next()


    aa = Myiterobj([3,4,5,6,7])
    for i in aa:
        print i


