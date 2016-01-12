# -*- coding:utf-8 -*-
"""
a.txt内容如下。xx为汉字。若最后一个数字相同，则按每一行第一个数字为准从小到大排序
2877,xx,xx,xx,xx,xx,xx,10
2878,xx,xx,xx,xx,xx,1264
2880,xx,xx,xx,xx,xx,xx,6
2881,xx,xx,xx,xx,xx,xx,xx,248
2882,xx,1
2887,xx,xx,xx,1
希望得到的结果存到b.txt 里边。内容如下：
2878,xx,xx,xx,xx,xx,1264
2881,xx,xx,xx,xx,xx,xx,xx,248
2877,xx,xx,xx,xx,xx,xx,10
2880,xx,xx,xx,xx,xx,xx,6
2882,xx,1
2887,xx,xx,xx,1
"""

rest = []
with open('spam.txt') as f:
    for line in f:
       linelist = line.strip('\n').split(',')
       line_rest = []
       for item in linelist:
           line_rest.append(int(item))
       rest.append(line_rest)
re_rest = sorted(rest, key=lambda x: x[-1],reverse=True)

with open('b.txt','w') as fb:
    for item in re_rest:
        item = str(item).strip('[ ]')
        fb.write(item+'\n')
