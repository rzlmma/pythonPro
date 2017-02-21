# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack

"""
检查输入的IP地址是否符合规范
"""

import re


def fileds_check(fields):
    pattern = '^((25[0-5]|2[0-4][0-9]|0|[1-9][0-9]?|1[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|0|[1-9][0-9]?|1[0-9][0-9]?)$'
    if re.match(pattern, fields):
        print "True"
    else:
        print "False"

if __name__ == '__main__':
    fileds_check('172.16.30.12')

