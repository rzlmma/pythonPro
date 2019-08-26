# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack

"""
检查输入的IP地址,电话号码，邮箱是否符合规范
"""

import re


def ip_check(fields):
    pattern = '^((25[0-5]|2[0-4][0-9]|0|[1-9][0-9]?|1[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|0|[1-9][0-9]?|1[0-9][0-9]?)$'
    if re.match(pattern, fields):
        print("True")
    else:
        print("False")


def phone_check(val):
    pattern = r'^1[3-9][0-9]{9}$'
    if re.match(pattern, val):
        print("True")
    else:
        print("False")


def email_check(val):
    pattern = r'^[a-z][a-z|0-9|.]*@163.com$'
    if re.match(pattern, val):
        print("True")
    else:
        print("False")


if __name__ == '__main__':
    ip_check('172.16.30.12')
    phone_check('18823456788')
    email_check('admin@163.com')

