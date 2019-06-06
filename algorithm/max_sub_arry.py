# -*- coding:utf-8 -*-
# __author__ = majing
"""
最大子数组
"""
import random

def find_mid_max_arry(alist, begin, mid, end):
    """
    找到最大中间子数组
    """
    left_max_num = alist[mid]
    right_max_num = alist[mid+1]
    left = mid
    right = mid+1

    total = 0
    for i in range(mid, begin-1, -1):
        total += alist[i]
        if left_max_num < total:
            left_max_num = total
            left = i

    total = 0
    for j in range(mid+1, end+1):
        total += alist[j]
        if right_max_num < total:
            right_max_num = total
            right = j

    max_num = left_max_num + right_max_num
    max_index = [left, right]
    return max_index, max_num


def find_max_array(alist, begin, end):
    if begin == end:
        return begin, alist[begin]
    else:
        mid = int((begin+end)/2)
        left_max_index, left_max_num = find_max_array(alist, begin, mid)
        print("begin:%s    mid:%s       left_max_index: %s    left_max_num:%s" % (begin, mid, left_max_index, left_max_num))

        right_max_index, right_max_num = find_max_array(alist, mid+1, end)
        print("mid+1:%s   end:%s   right_max_index: %s    right_max_num:%s" % (mid+1, end, right_max_index, right_max_num))

        mid_max_index, mid_max_num = find_mid_max_arry(alist, begin, mid, end)
        print("begin:%s   end:%s  mid_max_index: %s    mid_max_num:%s\n" % (begin, end, mid_max_index, mid_max_num))


        if left_max_num >= right_max_num and left_max_num >= mid_max_num:
            max_index= left_max_index
            max_num = left_max_num
        elif right_max_num >= left_max_num and right_max_num >= mid_max_num:
            max_index = right_max_index
            max_num = right_max_num
        elif mid_max_num >= left_max_num and mid_max_num >= right_max_num:
            max_index = mid_max_index
            max_num = mid_max_num
        print("begin:%s   end:%s   max_num:%s   max_index:%s" % (begin, end, max_num, max_index))
        return max_index, max_num




if __name__ == "__main__":
    alist = random.sample(range(-40, 50), 20)
    print("alist: ", alist)
    max_index, max_num = find_max_array(alist, 0, 19)
    print("last  max_index: %s    max_num:%s " % (max_index, max_num))

