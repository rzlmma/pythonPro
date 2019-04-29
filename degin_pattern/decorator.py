# -*- coding:utf-8 -*-
# __author__ = majing
"""
装饰器模式
"""


class Beverages(object):
    """
    饮料
    """
    description = ''

    def get_description(self):
        return self.description

    def cost(self):
        raise NotImplementedError()


class Condiment(Beverages):
    """
    调味料
    """

    def get_description(self):
        return self.description


class Espresso(Beverages):
    description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverages):
    """
    家庭混合
    """
    description = "HouseBlend"

    def cost(self):
        return 0.89


class Mocha(Condiment):
    description = "Mocha"

    def __init__(self, beverage):
        self.beverage = beverage

    def get_description(self):
        return self.description + " " + self.beverage.get_description()

    def cost(self):
        return 0.2 + self.beverage.cost()


if __name__ == "__main__":
    house_blent = HouseBlend()
    mocha_house_blend = Mocha(house_blent)
    cost = mocha_house_blend.cost()
    print(mocha_house_blend.get_description() + "  cost: %s" % cost)

    espresso = Espresso()
    mocha_espress = Mocha(espresso)
    cost = mocha_espress.cost()
    print(mocha_espress.get_description() + ' cost: %s ' % cost)



