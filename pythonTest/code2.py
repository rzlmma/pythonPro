# -*- coding:utf-8 -*-
"""
str1 = "爱情[love] 我们是好朋友 [smail]学习" 去掉str1中[]和[]里的内容
"""
def func(strParam):
    rest = []
    for k,v in enumerate(strParam):
        if v == '[' or v == ']':
            rest.append(k)
    #print "rest:",rest

    nstr = len(strParam)
    nrest = len(rest)

    res = ""
    res += strParam[0:rest[0]]

    for i in range(1,nrest-2,2):
        res += strParam[rest[i]+1:rest[i+1]]

    res += strParam[rest[nrest-1]+1:nstr]

    return res

if __name__ == "__main__":
    str1 = "爱情[love] 我们是好朋友 [smail]学习"
    print func(str1)