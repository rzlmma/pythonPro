#coding=utf-8
#求100以内的素数，以空格区分每个素数
alist =[]
for i in range(2,100):
    b = i//2
    for j in range(2, b+1):
        if i%j == 0:
            break
    else:
        alist.append(i)
        
print ' '.join([str(x) for x in alist])

#求解中位数

L=[1,2,3,4,5,6]
L.sort()
n = len(L)
middleN = 0
if n%2 == 0:
    a= n/2
    b= (n-2)/2
    middleN = (L[a]+L[b])/2.0
else:
    a = (n-1)/2
    middleN = L[a]
    
if type(middleN) == float:
    print '%.1f'%middleN
else:
    print middleN
    
 #结尾非零数的就行
 val =1
for i in L:
    val *= i   
a = val%10
while a==0:
     val = val/10
     a = val%10
if a%2 == 0:
    print '0'
else:
    print '1'
    
 #二进制数中1的个数
 res=[]
 n = 34
 a = n/2
 b = n%2
 res.append(b)
 while a != 0:
      b = a% 2
      a = a/2
      res.append(b)   
print res.count(1)

#求二进制的函数   b = bin(a)  type(b) == str
(2) b = bin(a)
res = []
for i in b:
   if i == '1':
       res.append()
print len(res)  or res.count('1')

#删除序列中的重复元素
L = [2,3,6,7,8,9,6,8,4,9]
alist = [1:]
i = L[0]
while alist:
     if i in alist:
          L.remove(i)
      i = alist[0]
      alist = alist[1:]
 print L
 
#实现min(), max()函数
def min(*pargs):
    pars = pargs
    res = pars[0]
    for item in pars[1:]:
        if item < res:
            res = item

    return res

def max(*pargs):
    res = pargs[0]
    for item in pargs[1:]:
        if item > res:
            res = item
    return res
    
def min2(*pargs):
    tmp = list(pargs)
    tmp.sort()
    return tmp[0]

def min3(first, *rest):
    for item in rest:
        if item < first:
            first = item
    return first
    
 #将求最大值和最小值放在一起
 def minmax(test, *pargs):
    res = pargs[0]
    for item in pargs[1:]:
        if test(item, res):
            res = item
    return res

def lessthan(x,y): return x < y

def graterthan(x,y): return x > y

 
 #求两个list的交集
 def share(alist, blist):
    res = []
    for i in alist:
        if i in blist:
           res.append(i)
    return res
    
    
#python3.0中print函数的实现
import sys
def print30(*args, **kargs):
    seq = kargs.get('seq', '')
    end = kargs.get('end', '\n')
    file = kargs.get('file', sys.stdout)
    output = ''
    first = True 
    for item in args:
        output += ('' if first else seq) + str(item)
        first = False 
    file.write(output+end)
    
 #模拟zip函数
 def myzip(*args):
    seqs = [list(s) for s in args]
    res = []
    while all(seqs):
       res.append(tuple(s.pop(0) for s in seqs))
    return res
    
#生成器模拟实现map
def mymap(*args, pad=None):
    seqs = [list(s) for s in args]
    while any(seqs):
       yield tuple((s.pop(0) if s else pad) for s in seqs)
       
