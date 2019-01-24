# -*- coding:utf-8 -*-
# __author__ = majing
"""
动态规划：钢条切割问题
"""
price = [1, 5, 8, 9, 10, 17, 17, 20, 24, 25]


def cut_rod(n):
    """
    递归 会重复计算最底层的值
    """
    if n == 0:
        return 0

    r = 0

    for i in range(1, n+1):
        val = price[i-1] + cut_rod(n-i)
        if val > r:
            r = val
            print("i:%s  n-i：%s val:%s" % (i, n - i, val))

    return r


def cut_rod_2(n, r):
    """
    自顶向下计算，记录已经计算过的值
    """
    if n == 0:
        r[0] = 0

    if r[n] > 0:
        return r

    p = 0

    for i in range(1, n+1):
        r = cut_rod_2(n - i, r)
        print("r: ", r)
        val = price[i-1] + r[n-i]
        if val > p:
            p = val
    r[n] = p
    return r


def cut_rod_bottom(n, r):
    for i in range(1, n+1):
        for j in range(i):
            if r[j] >= 0:
                continue
            r[j] = max(price[j], r[j])
    return r



if __name__ == "__main__":
    # rest = cut_rod(10)
    # print("rest: ", rest)

    r = [-1]*11
    rest = cut_rod_2(10, r)
    print("cut_rod_2: ", rest)

    rest = cut_rod_bottom(10, r)
    print("cut_rod_bottom: ", rest)