# -*- coding:utf-8 -*-
# __author__ = majing
"""
用二维数组来实现二叉树

[A, [B, None, None],
    [C, [D, None, None],
        [E, [F, None, None],
            [G, None, None]
        ]]
]

[root, lchid, rchild]
"""

class BtreeInterface(object):

    def __init__(self):
        self.root = None
        self.lchild = None
        self.rchild = None

    def create_tree(self, root, lchild=None, rchild=None):
        self.root = root
        self.lchild = lchild
        self.rchild = rchild
        return [self.root, self.lchild, self.rchild]

    def get_root(self, btree):
        return btree[0]

    def get_left_child(self, btree):
        return btree[1]

    def get_right_child(self, btree):
        return btree[2]

    def set_left_child(self, parent, btree):
        parent[1] = btree

    def set_right_child(self, parent, btree):
        parent[2] = btree

if __name__ == "__main__":

    bt = BtreeInterface()
    tree = bt.create_tree('A')
    tree_l_1 = bt.create_tree('B')
    tree_r_1 = bt.create_tree('C')

    bt.set_left_child(tree, tree_l_1)
    bt.set_right_child(tree, tree_r_1)

    t_l_2 = bt.create_tree('D')
    bt.set_left_child(tree_l_1, t_l_2)

    t_r_2 = bt.create_tree('E')
    bt.set_right_child(tree_l_1, t_r_2)

    print "tree: ", tree










