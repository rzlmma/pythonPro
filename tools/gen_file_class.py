# -*- coding:utf-8 -*-
# __author__ = majing
"""
获取一个文件中的所有的类或者某个类型的类
"""
import inspect
from abc import ABC


class Base(ABC):

    def test(self):
        print("<Base>.test")


class A(Base):
    def test(self):
        print("<A>.test")


class B(Base):
    def test(self):
        print("<B>.test")


def test():
    print("func test")


if __name__ == "__main__":
    values = [obj for obj in globals().values() if inspect.isclass(obj) and issubclass(obj, Base) and obj != Base]
    print("values: ", values)



