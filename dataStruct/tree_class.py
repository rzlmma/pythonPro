# -*- coding=utf-8 -*-
"""
二叉树基于链表的实现：data, right, left
"""

class BinTNode(object):
    def __init__(self, data, right=None, left=None):
        self.data = data
        self.right = right
        self.left = left
    def __str__(self):
        return "<BinTNode(%s)>" % self.data

class Btree(object):
    series = []
    @classmethod
    def create(cls, rnode, bletf, bright):
        rnode.left = bletf
        rnode.right = bright
        return rnode
    @classmethod
    def insert(cls, btree, node, left_or_right, new_node):
        exsits = cls.search(btree, node.data)
        if exsits:
            if left_or_right == 'left':
                if exsits.left:
                    raise ValueError('left node is already exsits')
            else:
                if exsits.right:
                    raise ValueError('right node is already exsits')
            setattr(exsits, left_or_right, new_node)
    @classmethod
    def search(cls, btree, value):
        cls.preorder_traverse(btree)
        for item in cls.series:
            if item.data == value:
                return item
    @classmethod
    def preorder_traverse(cls, btree):
        if btree is None:
            return []
        root = btree
        if root:
            cls.series.append(root)
            cls.preorder_traverse(root.left)
            cls.preorder_traverse(root.right)
        return cls.series

if __name__ == "__main__":
    nodes = []
    for i in range(10):
        nodes.append(BinTNode(i))

    t_1 = nodes[7]
    t_1.left = nodes[8]
    t_1.right = nodes[9]

    t_2 = nodes[2]
    t_2.left = nodes[5]
    t_2.right = nodes[6]

    nodes[6].left = t_1

    t_3 = nodes[1]
    t_3.left = nodes[3]
    t_3.right = nodes[4]

    root = nodes[0]
    root.left = t_3
    root.right = t_2

    print(Btree.preorder_traverse(root))

    print(Btree.search(root, 5))

    print(Btree.insert(root, nodes[6], 'left', BinTNode(10)))