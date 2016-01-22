# -*- coding:utf-8 -*-
"""
锚定码：
    ^       字符串或行的开始
    $        字符串或行的结尾
    \A       字符串开始
    \Z       字符串结尾
    \b        一个单词的开始或末尾空字符串
    \B        不在一个单词的开头或末尾空串

命名组:
(?P<name>pattern)
"""
import re
html_text = """
<div class="button"> submit
     <spam> test html <\spam>
<\div>

<div class='textarea'> name <\div>

<div class="button"> save <\div>
"""


def parse_html(patterns, text):
    for item in patterns:
        print "pattern:",item
        res = re.findall(item, text)
        print "findall:", res
        print "************************"


def se_groups(patterns, text):
    """
    group
    0  表示与整个表达式匹配的字符串
    子组按()出现的顺序，从左到右，从1开始标号
    """
    p = re.compile(patterns)
    m = p.search(text)
    print "groups:",m.groups()
    print "0:",m.group(0)           #返回匹配整个表达式的结果
    print "1:",m.group(1)           #返回与第一个分组匹配的结果
    print "2:",m.group(2)           #返回与第二个分组匹配的结果


def re_search():
    """
    re.IGNORECASE      #忽略大小写
    """
    text = "This is some text -- with punctuation"
    patt = r'\bT\w+'
    p = re.compile(patt)
    cp = re.compile(patt,re.IGNORECASE)
    print "=========without case=========="
    m = p.findall(text)
    print "findall:",m
    print "==========case============="
    cm = cp.findall(text)
    print "findall:",cm


if __name__ == '__main__':
    # parse_html([r'div class="button"', r'div class="button".*', r'div class="button".*<\\div>'], html_text)

    # pp = r'(\bt\w+)\W+(\w+)'
    # value = "This is some text -- with punctuation"
    # se_groups(pp, value)
    #
    # p = r'^(?P<first_word>\w+)'
    # m = re.search(p, value)
    # print m.group()
    # #选择
    # print re.findall(r'[rz|RZ]\w+', 'rzYma test RZmma')

    re_search()
