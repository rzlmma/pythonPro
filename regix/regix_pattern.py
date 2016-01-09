# -*- coding:utf-8 -*-
"""
正则表达式引擎---->编译表达式文本---->生成表达式对象------>匹配字符串------>匹配结果，返回匹配成功后的字符串，分组，索引
"""
import re
value = ['Python','welcome','python  pythoncode','happypython  pythonnew']
pattern = re.compile('python')
result = [re.search(pattern,item) for item in value]
print result
print "================================="
for item in result:
    if item is None:
        continue
    print"group:", item.group()
    print "re:",item.re
    print "groups:",item.groups()

ma = re.match(r'(\w+)(?P<sign> .*?)(\d+)','hello world 2016')

print "string:",ma.string
print "re:",ma.re
print "group:",ma.group(0,1)
print "groups:",ma.groups()

print "===============[]================"
ma2 = re.search(r'h[a-z]','wordhello happynew hidebutton')
print "string:",ma2.string
print "re:",ma2.re
print "group:",ma2.group(0)
print "groups:",ma2.groups()

print "==========split=============="
def test_split_findall():
    for item in [r'\d+', r'o', r'[a-z]']:
         p = re.compile(item)
         print "split:", p.split('one1two2three3four')
         print "findall", p.findall('one1two2three3four')
         print "*********************************"
