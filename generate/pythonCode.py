# -*- coding:utf-8 -*-
"""
python 高级编程收录
"""
#生成器,throw
def my_generate():
    try:
        yield "somthing"
    except ValueError:
        yield "dealing with something"
    finally:
        print "let's clean"

#生成器为一个表达式
def my_generate2():
    print "please tell me you problems"
    while True:
        answer =(yield)
        if answer.endswith('?'):
            print "don't ask yourself too mush questions"
        elif 'good' in answer:
            print "A that's good,go on"
        elif 'bad' in answer:
            print "don't be so negative"
        else:
            print "the test is ending"

#生成器表达式
from __future__ import print_function
def func():
    for i in (item for item in range(100) if item%2 ==0):
        print (i,end=',')


if __name__ == "__main__":

    # gn = my_generate()
    # gn.next()
    # print gn.throw(ValueError('test'))
    # gn.close()
    gn = my_generate2()
    gn.next()
    gn.send('food is good')
    gn.send('bad')
    gn.send('what show I do ?')
    gn.send('test')
