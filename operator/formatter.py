# -*- coding:utf-8 -*-
"""
自定义格式化输出
"""
_formats ={
    'ymd': '{d.year}-{d.month}-{d.day}',
    'myd': '{d.month}/{d.year}/{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}'
}
class MyDate(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

if __name__ == '__main__':
    d = MyDate(2015,12,5)
    print format(d)
    print format(d,'myd')
    print "this date is {:mdy}".format(d)