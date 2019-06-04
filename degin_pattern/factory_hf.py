# -*- coding:utf-8 -*-
# __author__ = majing
"""
head first设计模式  工厂模式
"""

class PizzaStore(object):

    def order_pizza(self, p_type):
        p = self.create_pizza(p_type)
        if not p:
            return '[%s] is not exists'

        p.prepare()
        p.bake()
        p.cut()
        p.box()
        print('[%s] is OK' % p_type)

    def create_pizza(self, p_type):
        raise NotImplementedError()


class Pizza(object):
    name = ''
    dough = ''
    sauce = ''

    def prepare(self):
        print("Prepare " + self.name)
        print("Tossiong dough " + self.dough)
        print("Adding sauce " + self.sauce)

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("place pizza in official pizzastore box")

    def get_name(self):
        return self.name


class NYStyeCheesePizza(Pizza):
    name = "NY Style Sauce and Cheese Pizza"
    dough = "Thin Crust Dough"
    sauce = "Marinara Sauce"


class NYStyleVeggiePizza(Pizza):
    pass

class NYStylePepperoniPizza(Pizza):
    pass


class NYPizzaStore(PizzaStore):

    def create_pizza(self, p_type):
        if p_type == 'cheese':
            return NYStyeCheesePizza()
        elif p_type == 'veggie':
            return NYStyleVeggiePizza()

        elif p_type == 'pepperoni':
            return NYStylePepperoniPizza()
        else:
            return None
