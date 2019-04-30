# -*- coding:utf-8 -*-
# __author__ = majing
"""
策略模式
"""


class Duck(object):

    def __init__(self, fly, quack):
        self.fly = fly
        self.quack = quack

    def perform_quack(self):
        self.quack.quack()

    def perform_fly(self):
        self.fly.fly()

    def display(self):
        raise NotImplementedError()

    def swim(self):
        print("all ducks float, even decoys")


class MallarDuck(Duck):

    def display(self):
        print("this is a real Mallard duck")


class FlyBehavior(object):

    def fly(self):
        raise NotImplementedError()


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying")


class FlyNoway(FlyBehavior):
    def fly(self):
        print("I'm can't fly")


class QuckBehavior(object):

    def quack(self):
        raise NotImplementedError()


class Quack(QuckBehavior):
    def quack(self):
        print("Quack")


class Squeak(QuckBehavior):
    def quack(self):
        print("Squeak")


if __name__ == "__main__":

    fly = FlyWithWings()
    quack = Squeak()

    mallard = MallarDuck(fly, quack)
    mallard.perform_fly()
    mallard.perform_quack()
