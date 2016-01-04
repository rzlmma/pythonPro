# -*- coding:utf-8 -*-
"""
创建一个pizza shop，有server，chef
"""
class Employee:
    def __init__(self,name,salary=0):
        self.name = name
        self.salary = salary

    def giveRaise(self,percent):
        self.salary = self.salary + self.salary * percent

    def work(self):
        print "%s does stuff"%(self.name)

    def __repr__(self):
        return "<%s: name=%s salary=%s>"%(self.__class__, self.name, self.salary)

class Chef(Employee):
    def __init__(self,name):
        Employee.__init__(self,name,5000)

    def work(self):
        print"Chef:%s make foods"%(self.name)


class Server(Employee):
    def __init__(self,name, salary=4000):
        Employee.__init__(self,name,salary)

    def work(self):
        print "Server:%s interface with the customer"%(self.name)


class PizzaRobot(Chef):
    def __init__(self,name):
        Chef.__init__(self,name)

    def work(self):
        print "PizzaRobot:%s make pizza"%(self.name)


