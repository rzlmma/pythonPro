# -*- coding:utf-8 -*-
# __author__ = majing
"""
字段序比较2个字符串的大小
"""

def compare(str1, str2):
    count = min(len(str1), len(str2))

    for i in range(count):
        if str1[i] > str2[i]:
            return True
        elif str1[i] < str2[i]:
            return False

    return len(str1) > len(str2)

if __name__ == "__main__":
    print("compare('adfghj', 'awer'):", compare('adfghj', 'awer'))
    print("compare('awer', 'awer'): ", compare('awer', 'awer'))
    print("compare('aweq', 'awerq'): ", compare('awey', 'awerq'))



