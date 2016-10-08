# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
import sys


class Render(object):

    def header(self, title):
        pass

    def paragraphs(self, paragraph):
        pass

    def footer(self):
        pass


class Page(object):
    def __init__(self, title, renderer):

        if not isinstance(renderer, Render):
            raise TypeError("Except a Render object")

        self.title = title
        self.render = renderer
        self.paragraphs = []

    def get_paragraphs(self, paragraph):
        self.paragraphs.append(paragraph)

    def render(self):
        self.render.header(self.title)
        for item in self.paragraphs:
            self.render.paragraphs(item)
        self.render.footer()
