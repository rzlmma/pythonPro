# -*- coding:utf-8 -*-
"""
快速排序
"""
def partions(alist, p, r):
    i = p -1
    key = alist[r]
    for j in range(p,r):
        if alist[j] <= key:
            i = i+1
            alist[i], alist[j] = alist[j], alist[i]
    alist[i+1], alist[r] = alist[r], alist[i+1]
    return i+1


def quick_sort(alist, p, r):
    if p < r:
        q = partions(alist, p, r)
        quick_sort(alist, p, q-1)
        quick_sort(alist, q+1, r)

if __name__ == "__main__":
    import random
    alist = random.sample(range(100),20)
    print("befor sort: ", alist)
    quick_sort(alist, 0, 19)
    print("after sort: ", alist)


