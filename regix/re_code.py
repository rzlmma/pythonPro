# -*- coding:utf-8 -*-
"""
字符集
    字符集是一组字符，包含可以与模式中相应位置匹配的所有字符
    [a,b] 匹配a or b
    [^ab]   匹配不在字符集中出现的字符
    字符区间来定义字符集，其中包含一个起点和终点之间连续的字符
转义码
    \d     数字
    \D     非数字
    \w     字母数字
    \W      非字母数字
    \s      空白符(\n \t whitespace)
    \S      非空白符
"""
from code import test_regix

values = ['abbaabbbbaa', 'abbaasbbbaa']
for text in values:
    test_regix([('[a,b]', 'a or b'),
               ('a[a,b]', 'a followed by a or b'),
               ('a[a,b]+', 'a followed by a or b one or more times'),
               ('a[a,b]+?', 'a followed by a or b one time')
                ],
               text
               )
    print '\n'

print '\n'

test_regix([('[^-,. ]+', '除了-,. 空格'), ('[^-. ]+', '除了-.空格')], 'this is -- my hose, yellow,red, blue.')

print"=========测试字符区间========"
test_regix([('[a-zA-Z]+', 'a-z and A-Z'),
            ('[a-z]+',  'a-z'),
            ('[A-Z][a-z]+', 'A-Z a-z'),
            (r'\w+', '字母 数字')
            ],
           'this is -- My@Hose, yellow2red, Blue.')
