# -*- coding:utf-8 -*-
"""
基本工厂模式
"""
class FactoryPattern(object):

    def create_button(self, param):
        typeclass = param.capitalize()
        return globals()[typeclass]()


class Button:
    html = '<button></button>'

    factory = FactoryPattern()

    def get_html(self, b_type):
        button = self.factory.create_button(b_type)
        return button.html


class Image(Button):
    html = "<img alt= \>"


class Input(Button):
    html='<input type="text" >'


class Falsh(Button):
    html = ''




if __name__ == "__main__":

    b = Button()
    html = b.get_html('image')
    print(html)
