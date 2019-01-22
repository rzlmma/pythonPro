# -*- coding:utf-8 -*-
"""
分治算法: 最大子数组的和
思想：
最大子数组存在三种可能的情况：
    在数组的左侧             数组的右侧               跨数组中心

"""
import random

def find_max_crossing_subarray(alist, low, mid, high):
    left_sum = float("-inf")
    max_left = sum = 0
    for i in range(mid, low-1, -1):
        sum += alist[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = float("-inf")
    max_right = sum = 0
    for j in range(mid+1, high+1):
        sum += alist[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j

    return (max_left, max_right, left_sum+right_sum)


def find_maximum_subarray(alist, low, high):
    if low == high:
        return (low, high, alist[low])
    else:
        mid = (low + high)/2
        (left_low, left_high, left_sum) = find_maximum_subarray(alist, low, mid)
        (right_low, right_high, right_sum) = find_maximum_subarray(alist, mid+1, high)
        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(alist, low, mid, high)
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

if __name__ == "__main__":
    alist = random.sample(range(-100, 100) , 20)
    print("alist:", alist)
    print(find_maximum_subarray(alist, 0, 19))
