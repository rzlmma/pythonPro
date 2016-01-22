# -*- coding:utf-8 -*-
"""
异常
1.错误处理
     当发生错误的时候，python会跳到try处理器，处理错误。try之后的语句会继续运行
2.时件通知
3.特殊情况处理
4.终止行为
     try/finally 不管是否发生异常，finally中的语句一定会执行
5.非常规控制流程
"""
import sys
x = [2,3,4,5]
try:
    aa = x[4]
except IndexError:
    aa = 23

bb = aa*3
print bb

#try/except/else/finally
sep = '-'*32 + '\n'
print sep + "exception raised and caught"
X = 'spam'
try:
    X[4]
except IndexError:
    print "caught exception and do it:",sys.exc_info()

else:
    print "X[4]:",X[4]
finally:
    print 'finally run'
print 'after run'

print sep + 'no exception raised'
try:
    X[3]
except IndexError:
    print "caught exception and do it"
else:
    print "X[3]:",X[3]
finally:
    print 'finally run'
print 'after run'

print sep + 'exception raised but not caught '
try:
    X[4]
except ValueError:
    print "caught exception and do it"
else:
    print "X[4]:",X[4]
finally:
    print "finally run"
print "after run"