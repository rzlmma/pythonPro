# -*- coding:utf-8 -*-
"""
有一个列表：[1,2,3,...n],n=20,请编写代码打印如下规律的输出：
1[1*,2,3,4,5]
2[1,2*,3,4,5]
3[1,2,3*,4,5]
4[2,3,4*,5,6]
5[3,4,5*,6,7]
6[4,5,6*,7,8]
...
20[16,17,18,19,20*]
"""
def printFunc(n):
    rest = {}
    for i in range(1,n+1):
        if i==1:
           rest[i] = "[1*,2,3,4,5]"
        elif i==2:
            rest[i] = "[1,2*,3,4,5]"
        elif i==3:
            rest[i] = "[1,2,3*,4,5]"
        elif i>3 and i<=18:
            rest[i] = "[%s,%s,%s*,%s,%s]"%(i-2,i-1,i,i+1,i+2)
        elif i==19:
            rest[i] = "[16,17,18,19*,20]"
        else:
            rest[i] = "[16,17,18,19,20*]"
    return rest

if __name__ == "__main__":
   valuesTuple = printFunc(20).items()
   for item in valuesTuple:
       print "%d:%s"%(item[0],item[1])

