# -*- coding:utf-8 -*-
# __author__ = majing

import copy
"""
求二叉树的所有路径
     15
    /  \
   20   6
  /  \   \
 8   10  40
 /\   \    / \
22 23 18   9  12
思路:
2个列表
1.记录到达本节点时之前的节点    2.记录路径           
"""
# 构造一棵树
class Node(object):
    """
    节点
    """
    def __init__(self, left, right, data):
        self.data = data
        self.left = left
        self.right = right


class Tree(object):
    def add_root(self, node):
        self.root = node

    def add_left_tree(self, node, n_node):
        node.left = n_node

    def add_right_tree(self, node, n_node):
        node.right = n_node


tree = Tree()
node = Node(None, None, 15)
tree.add_root(node)

node_8_22 = Node(None, None, 22)
node_8_23 = Node(None, None, 23)
node_10_18 = Node(None, None, 18)

node_40_9 = Node(None, None, 9)
node_40_12 = Node(None, None, 12)

node_1 = Node(node_8_22, node_8_23, 8)
node_2 = Node(None, node_10_18, 10)
node_3 = Node(None, None, 20)

node_4 = Node(node_40_9, node_40_12, 40)
node_5 = Node(None, None, 6)


tree.add_left_tree(tree.root, node_3)
tree.add_left_tree(tree.root.left, node_1)
tree.add_right_tree(tree.root.left, node_2)

tree.add_right_tree(tree.root, node_5)
tree.add_right_tree(tree.root.right, node_4)


def get_all_path(node, before_nodes, paths):
    new_str = copy.deepcopy(before_nodes)
    if node.left is None and node.right is None:
        paths.append(before_nodes)
        return paths

    if node.left:
        before_nodes.append(node.left.data)
        get_all_path(node.left, before_nodes, paths)

    if node.right:
        new_str.append(node.right.data)
        get_all_path(node.right, new_str, paths)

    return paths


def binary_tree_path():
    before_nodes = []
    paths = []
    before_nodes.append(tree.root.data)
    get_all_path(tree.root, before_nodes, paths)
    return paths


if __name__ == "__main__":
    paths = binary_tree_path()
    print("paths: ", paths)

