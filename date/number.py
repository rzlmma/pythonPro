# -*- coding:utf-8 -*-
"""
处理数字的函数
执行分数运算的模块 fraction
随机选择 random
"""
from fractions import Fraction
import random
#四舍五入
num1 = round(3.234,2)

#二八十六进制
bin(34)
hex(34)
oct(34)

#foramt可以去掉'0b','o','0x'
format(34, 'b')
format(34, 'o')
format(34, 'x')

#分数运算
num1 = Fraction(5,4)
num2 = Fraction(7,20)
num = num1+num2
print "--------------分数运算--------------"
print "num:",num
print "分子：",num.numerator
print "分母:", num.denominator


print "-----------------随机选择-----------------"
value = ['a','b','d','e','f','g']

#随机抽取一个元素
print random.choice(value)

#提取N个不同的元素
print random.sample(value,2)
print random.sample(value,4)

#打乱元素的顺序
random.shuffle(value)
print "value:",value
random.shuffle(value)
print 'value:',value

#随机生成一个整数
print random.randint(2,9)

#生成0,1之间的浮点数
print random.random()

#获取N为随机位(二进制)的整数
print random.getrandbits(8)






