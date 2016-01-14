# -*- coding:utf-8 -*-
"""
通过定义4个类，来模拟订餐场景
"""
class Lunch:
    def __init__(self,customer, employee):
        self.customer = customer
        self.employee = employee


    def order(self,foodName):
        self.customer.placeOrder(foodName, self.employee)


    def result(self):
        print "Order:"
        print "customer: %s" %(self.customer.name)
        self.customer.printFood()
        print "server:",self.employee.name
        print "============================"

class Customer:
    def __init__(self,name):
        self.name = name

    def placeOrder(self, foodName,employee):
        self.foodname = foodName
        employee.takeOrder(foodName)

    def printFood(self):
        print "food name:",self.foodname

class Employee:
    def __init__(self,name):
        self.name = name

    def takeOrder(self,foodName):
        return Food(foodName)

    def __str__(self):
        return '<employee> %s'%(self.name)

class Food:
    def __init__(self,name):
        self.name = name

if __name__ == "__main__":
    emplyee = Employee('Bob')
    customer = Customer('Jhon Smth')
    order = Lunch(customer,emplyee)
    order.order('hai xian')
    order.result()