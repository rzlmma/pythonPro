# -*- coding:utf-8 -*-
"""
抽象工厂模式
"""
from random import choice

class PetShop:
    def __init__(self, animal_factory=None):
        self.animal_factory = animal_factory

    def show_pet(self):
        animal = self.animal_factory.get_pet()
        print "the animal is:",animal.__class__
        print "the animal speak:",animal.speak()
        print "the animal food:",self.animal_factory.get_food()
        print "the pet color:", animal.color()


class Dog:
    _color = ['yellow','white','black','blue']
    def speak(self):
        return "woof"
    def __str__(self):
        return "dog"

    def color(self):
        self.color = choice(Dog._color)
        return self.color


class Cat:
    _color = ['yellow','white','black']
    def speak(self):
        return "miao"
    def __str__(self):
        return "cat"
    def color(self):
        self.color = choice(Cat._color)
        return self.color


class DogFactory:
    def get_pet(self):
        return Dog()
    def get_food(self):
        return "dog food"


class CatFactory:
    def get_pet(self):
        return Cat()
    def get_food(self):
        return "cat food"


def get_factory():
    return choice([DogFactory,CatFactory])()


if __name__ == "__main__":
    shop = PetShop(DogFactory())
    shop.show_pet()

    print "====================="

    shop = PetShop()
    shop.animal_factory = get_factory()
    shop.show_pet()