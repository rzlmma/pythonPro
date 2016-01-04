# -*- coding:utf-8 -*-
"""
pizzaShop: customer
"""
from random import randint
from employee import Server,PizzaRobot
class Customer:
    def __init__(self,name):
        self.name = name

    def order(self, server,pizza_name,pizza_size):
        print "%s order from the [server] %s"%(self.name,server.name)
        pizza = Pizza(pizza_name,pizza_size)
        pizza_info = pizza.pizza_info
        if pizza_info.has_key(pizza_name):
            if pizza_info.get(pizza_name).has_key(pizza_size):
                print "[pizza_name] -- %s  [pizza_size] -- %s"%(pizza_name,pizza_size)
            else:
                raise ValueError("we don't have the pizza,please choose a new pizza")
        else:
            raise ValueError("we don't have the pizza,please choose a new pizza")

    def pay(self, server,pizza_name,pizza_size):
        pizza = Pizza(pizza_name, pizza_size)
        price = pizza.getPrice()
        print "%s pay to the [server] %s, [price] %s"%(self.name, server.name,price)

class Pizza:
    pizza_info = {'pizza_1':{'9':32, '12':45}, 'pizza_2':{'9':24, '12':34}, 'pizza_3':{'9':48, '12':56}}
    def __init__(self, pizza_name='', pizza_size=''):
        self.pizza_name = pizza_name
        self.pizza_size = pizza_size

    def getPrice(self):
        price = Pizza.pizza_info.get(self.pizza_name).get(self.pizza_size)
        return price

    def addPizza(self,name,size,price):
        pizzaInfos = Pizza().pizza_info
        if name in pizzaInfos.keys():
            pizzaInfos[name].update({size: price})
        else:
            pizzaInfos[name] = {size: price}
class PizzaShop:
    def __init__(self):
        self.server = [Server('Bob')]
        self.chef = PizzaRobot('Spam')

    def order(self, name,pizza_name, pizza_size):
        print"order:"
        customer = Customer(name)
        count_server = len(self.server)
        index = randint(0, count_server-1) if count_server > 1 else 0
        customer_server = self.server[index]
        customer.order(customer_server,pizza_name,pizza_size)
        self.chef.work()
        customer.pay(customer_server,pizza_name,pizza_size)

    def addServer(self, server):
        if isinstance(server, Server):
            self.server.append(server)
        else:
            raise ValueError('the argument need a instance of Server')

if __name__ == "__main__":
    shop = PizzaShop()
    shop.order('Samth','pizza_2','9')

    shop.addServer(Server('Joe'))
    shop.addServer(Server('Jhon'))

    shop.order('Lucy','pizza_1','12')

    Pizza().addPizza('pizza_4','24',67)
    print Pizza().pizza_info
    Pizza().addPizza('pizza_4','14',34)
    print Pizza().pizza_info