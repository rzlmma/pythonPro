# -*- coding:utf-8 -*-
# __author__ = majing
"""
矩阵乘法
"""
import numpy as np

matrix_A = np.arange(32, dtype=int).reshape(4, 8)
print "matrix_A: ", matrix_A

matrix_B = matrix_A.T
print "matrix_B: ", matrix_B

matrix_C = np.empty((4, 4))


for i in range(4):
    for j in range(4):
        sum = 0
        for k in range(8):
            sum += matrix_A[i][k] * matrix_B[k][j]
        matrix_C[i][j] = sum

print "matrix_C: ", matrix_C

