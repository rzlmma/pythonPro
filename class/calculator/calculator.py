# -*- coding:utf-8 -*-
"""
实现一个简易的计算器，实现+ - * / **
当lnum rnumd都为0时，退出
"""
OPERATORS = ['+', '-', '*', '/', '**']
class Calculator:
    def __init__(self,lnum=0, operator=None, rnum=1):
        self.lnum = lnum
        self.operator = operator
        self.rnum = rnum
    def show_result(self):
        result = self.operator.get_result(self.lnum, self.rnum)
        print "{0} {1} {2} = {3}".format(self.lnum, self.operator._oper, self.rnum, result)

class Adder:
    _oper = '+'
    def get_result(self,lnum, rnum):
        return lnum + rnum

class Sub:
    _oper = '-'
    def get_result(self,lnum, rnum):
        return lnum - rnum

class Mutil:
    _oper = '*'
    def get_result(self,lnum, rnum):
        return lnum*rnum

class Division:
    _oper = '/'
    def get_result(self,lnum, rnum):
        if rnum == 0:
            raise ValueError('/ rnum not 0')
        return lnum/rnum

class Power:
    _oper = '**'
    def get_result(self,lnum, rnum):
        return lnum**rnum
def get_operator_nums():
    print"Note: the expression contains two numbers and a operator"
    result = raw_input('please input a expression:')
    if result.endswith('='):
        result = result[:-1]

    opt = filter(lambda y: y in OPERATORS, filter(lambda x: x.isdigit()== False, result))
    operator = opt if opt else ' '
    lnum, rnum = result.split(operator) if len(result.split(operator))==2 else ('0', '0')
    # print "lnum:%s  rnum:%s"%(lnum,rnum)
    if not lnum.isdigit():
        return get_operator_nums()
    if not rnum.isdigit():
        return get_operator_nums()
    return int(lnum),operator,int(rnum)



if __name__ == "__main__":
    operatorInfo = {
        '+': Adder,
        '-': Sub,
        '*': Mutil,
        '/': Division,
        '**': Power
    }
    while True:
         lnum, operator, rnum = get_operator_nums()
         if lnum == 0 and rnum == 0:
             print "ending!!!!!!!!!!"
             break
         operatorClass = operatorInfo.get(operator,Adder)()
         cal = Calculator(lnum,operatorClass,rnum)
         cal.show_result()
         print "="*20