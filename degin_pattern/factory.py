# -*- coding:utf-8 -*-
"""
工厂模式
"""
class Button:
    html = '<button></button>'
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img alt= \>"

class Input(Button):
    html='<input type="text" >'

class Falsh(Button):
    html=''

class FactoryPattern():
    def create_button(self, param):
        typeclass = param.capitalize()
        return globals()[typeclass]()

if __name__ == "__main__":
    obj = FactoryPattern()
    html= obj.create_button('image').get_html()
    print html
    print globals()  #获取模块中所有的全局变量
