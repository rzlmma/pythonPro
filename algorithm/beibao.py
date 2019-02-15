# -*- coding:utf-8 -*-
# __author__ = majing
"""
01背包问题 
描述
  有编号分别为n[i]的五件物品，它们的重量分别是6, 9, 14, 16, 19，它们的价值分别是8, 13, 25, 44, 22，现在给你个承重为30的背包，
  如何让背包里装入的物品具有最大的价值总和？
"""
total = 11       #背包能容纳的重量
n = 5       #物品的数量
w = [5,4,7,2,6]         #每件物品的重量
p = [12,3,10,3,6]          #每件物品的价值

rest = [[0]*(total+1) for i in range(n+1)]      # 初始化一个二维数组，rest[i][w] (i=0,1,2,3,4,5   w=0,1,2,3,4,...11)
f = [0] * (total+1)


def pack():
    """
    :param n: 物品的数量
    :param total: 背包能容纳的重量
    """
    for i in range(1, n+1):
        for j in range(total+1):
            if w[i-1] > j:
                rest[i][j] = rest[i-1][j]
            else:
                if j-w[i-1] >= 0:
                    rest[i][j] = max(rest[i-1][j-w[i-1]]+p[i-1], rest[i-1][j])
    return rest


def pack_2():
    """
    优化空间复杂度之后的算法   O(total+1)
    :return: 
    """
    for i in range(1, n+1):
        for j in range(total, w[i-1]-1, -1):
            f[j] = max(f[j], f[j - w[i - 1]] + p[i - 1])

    return f



if __name__ == "__main__":
    rest = pack()
    print("rest: ", rest)

    rest = pack_2()
    print("pack_2: ", rest)















