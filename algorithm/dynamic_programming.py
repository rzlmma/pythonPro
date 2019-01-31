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
    """
    没种长度的最优解的切割方案
    """
    r[0] = 0
    for i in range(1, n+1):
        p = 0
        for j in range(1, i+1):
            if p < (price[j-1]+r[i - j]):
                p = price[j-1]+r[i - j]
                s[i] = ("n:%s" %i, (j, i - j), "p:%s" % p)

        r[i] = p
    return r



if __name__ == "__main__":
    # rest = cut_rod(10)
    # print("rest: ", rest)

    r = [-1]*11
    s = [0] * 11
    # rest = cut_rod_2(10, r)
    # print("cut_rod_2: ", rest)

    rest = cut_rod_bottom(10, r)
    print("cut_rod_bottom: ", rest)
    print("cut_rod_bottom: ", s)