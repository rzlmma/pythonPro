# -*- coding:utf-8 -*-
import difflib

text1 = """
Explicit is better than implicit.
Sparse is better than dense.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Namespaces are one honking great idea -- let's do more of those! python 哲学
"""
text1_lines = text1.splitlines()

text2 = """
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Sparse is better than dense.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
Namespaces are one honking great idea -- let's do more of those!
"""
text2_lines = text2.splitlines()

d = difflib.Differ()
diff = d.compare(text1_lines, text2_lines)
print '\n'.join(diff)

print "=="*9

diff = difflib.unified_diff(text1_lines, text2_lines, lineterm='')
print '\n'.join(diff)

print "=="*9

A = 'asss bhtfg\t bnmkl'
B = 'asss bht bnmkl'
df = difflib.ndiff(A,B)    #ndiff默认忽略空格和制表符
print '\n'.join(df)

