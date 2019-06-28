# -*- coding:utf-8 -*-
# __author__ = majing
"""
二叉搜索树
"""

def search(root, key):
    if root is None:
        return False, None

    if root.data == key:
        return True, root

    if key < root.data:
        return search(root.left, key)

    return search(root.right, key)


def process(root):
    if root:
        process(root.left)
        print(root.data)
        process(root.right)


def non_search(root, key):
    if root is None:
        return False, None

    while root:
        if root.data == key:
            return True, root

        if key < root.data:
            root = root.left
        else:
            root = root.right


def min_data(root):
    while root:
        root = root.left
    return root

def max_data(root):
    while root:
        root = root.right
    return root


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    if len(s) % 2 != 0:
        mid = int((len(s) - 1) / 2)
    else:
        mid = int((len(s) - 2) / 2)

    print("mid: ", mid)
    for i in range(1, mid+1):
        if len(s) % 2 != 0:
            print("mid-i:%s   mid+i:%s " % (mid-i, mid+i))
            s[mid - i], s[mid + i] = s[mid + i], s[mid - i]
        else:
            s[mid - i], s[mid + i + 1] = s[mid + i + 1], s[mid - i]
    return s


s = ["h","e","l","l","o"]
print("befor s: ", s)
print('s: ', reverseString(s))