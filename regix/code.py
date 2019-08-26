# -*- coding:utf-8 -*-
"""
重复匹配：
1.*  出现0 or more
2.+  至少出现一次
3.？ 0 or more
4.{m}  出现m次
5.{m,n}  出现的次数在m~ n 范围内;若果省略n,则至少出现m次，无上限
6. .  匹配所有的单字符
"""
import re
def test_regix(patterns, text):
    for pattern ,label in patterns:

        math_strings = re.findall(pattern, text)

        # print "$$"*6
        # se = re.search(pattern, text)
        # match_groups = se.groups()
        # print 'search groups:',match_groups
        # print "$$"*6

        match = re.finditer(pattern, text)
        for item in match:
            s = item.start()
            e = item.end()


if __name__ == '__main__':
    # 尽可能多的匹配
    test_regix([('ab*', 'a followed by b zero or more times'),
            ('ab+', 'a followed by b one or more times'),
            ('ab?', 'a followed by b zero or more times'),
            ('ab{3}', 'a followed by b three times'),
            ('ab{2,3}', 'a followed by b two to three times')
            ],
            'abbaabbbbbaaa'
    )

    print("========禁用贪心匹配=======")
    # 禁用贪心匹配模式
    test_regix([('ab*?', 'a followed by b zero or more times'),  #b出现0次
            ('ab+?', 'a followed by b one or more times'),       #b出现1次
            ('ab??', 'a followed by b zero or more times'),      #b出现0次
            ('ab{3}?', 'a followed by b three times'),           #b出现3次
            ('ab{2,3}?', 'a followed by b two to three times')   #b出现2-3次
            ],
            'abbaabbbbbaaa'
    )


