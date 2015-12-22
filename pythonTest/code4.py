# -*- coding:utf-8 -*-
"""
将驼峰命名法字符串转换成下划线命名法
eg. GetItem ---> get_item
    getIT   ----> get_it
"""
def changeStr(param):
    rest = []
    for k,v in enumerate(param):
        if v.isupper():
            rest.append(k)
    print rest

    nrest = len(rest)
    nparam = len(param)
    res = ""
    if rest[0] == 0:
        for i in range(0,len(rest)-1):
            res += param[rest[i]:rest[i+1]]
            if rest[i+1] - rest[i] == 1:
                continue
            res += "_"
        res += param[rest[nrest-1]:nparam]
    else:
        res += param[0:rest[0]]
        res += "_"
        for i in range(0,len(rest)-1):
            res += param[rest[i]:rest[i+1]]
            if rest[i+1] - rest[i] == 1:
                continue
            res += "_"
        res += param[rest[nrest-1]:nparam]
    return res.lower()

if __name__ == "__main__":
    print changeStr("heGetItEmQY")
    print changeStr("GetItem")