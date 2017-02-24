# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack
""""
双链表  search, insert, delete
"""


class Node(object):
    def __init__(self, value=None):
        self._prev = None
        self.data = value
        self._next = None

    def __str__(self):
        return "Node(%s)"%self.data


class DoubleLinkedList(object):
    def __init__(self):
        self._head = Node()

    def insert(self, value):
        element = Node(value)
        element._next = self._head
        self._head._prev = element
        self._head = element

    def search(self, value):
        if not self._head._next:
            raise ValueError("the linked list is empty")
        temp = self._head
        while temp.data != value:
            temp = temp._next
        return temp

    def delete(self, value):
        element = self.search(value)
        if not element:
            raise ValueError('delete error: the value not found')
        element._prev._next = element._next
        element._next._prev = element._prev
        return element.data

    def __str__(self):
        values = []
        temp = self._head
        while temp and temp.data:
            values.append(temp.data)
            temp = temp._next
        return "DoubleLinkedList(%s)"%values


if __name__ == "__main__":
    d = DoubleLinkedList()
    d.insert(2)
    d.insert(6)
    d.insert('hello')
    d.insert(90)
    print "DoubleLinkedList:",d

    print "delete 6:"
    d.delete(6)
    print "DoubleLinkedList:", d