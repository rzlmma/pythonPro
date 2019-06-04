# -*- coding:utf-8 -*-
# __author__ = majing

def merge(l, begin, q, end):
    """
    合并2个有序的数组
    """
    print("merge====> begin:%s    q:%s    end:%s\n" % (begin, q, end))
    l1 = l[begin:q+1]
    l2 = l[q+1:end+1]

    len_1 = len(l1)
    len_2 = len(l2)

    i, j, m = 0, 0, 0
    for k in range(begin, end+1):
        if i < len_1 and j < len_2:
            if l1[i] < l2[j]:
                l[k] = l1[i]
                i += 1
            else:
                l[k] = l2[j]
                j += 1
            m = k

    m = m + 1

    if i < len_1:
        while i < len_1:
            l[m] = l1[i]
            m += 1
            i += 1

    if j < len_2:
        while j < len_2:
            l[m] = l2[j]
            j += 1
            m += 1

    print("l: %s\n" % l)


def func(alist, begin=0, end=0):
    q = int((begin+end)/2)
    if q < end:
        print("begin:%s   q:%s  end:%s" % (begin, q, end))

        func(alist, begin, q)
        func(alist, q+1, end)

        merge(alist, begin, q, end)


if __name__ == "__main__":
    aa = [34, 2, 89, 45, 12, 6, 9, 10, 33, 88, 24, 16]
    func(aa, 0, len(aa)-1)
