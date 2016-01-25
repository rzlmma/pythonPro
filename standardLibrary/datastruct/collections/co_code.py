# -*- coding:utf-8 -*-
"""
容器数据集
Counter:  序列，字典，关键字参数
>>> Counter()
>>> Counter('asdfgh')
>>> Counter(a=2,b=3,c=4)
>>> Counter({'a':2, 'b':3})
"""
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict
import threading, time
def init():
    c = Counter()
    c.update(a=3, b=4, c=1, d=2)
    c.update('aabcd')
    print c, c['a'], c['e']
    #most_common
    for p in [None,2,3]:
        print "%s: %s"%(p, c.most_common(p))


def oper_counter():
    c1 = Counter('welcometochinae')
    c2 = Counter('happynewyear')
    print "c1:",c1
    print 'c2:',c2
    for item in ['c1&c2', 'c1|c2', 'c1+c2', 'c1-c2', 'c1==c2', 'c1>c2']:
        print "%s: %s"%(item, eval(item))

#defaultdict
def default_factory():
    return 'happy new year'

def init_d():
    d = defaultdict(default_factory, a='yellow', b='blue')
    print d
    for p in ['a','b','c']:
        print "d[{0}]: {1}".format(p, d[p])

#deque  双端队列
def init_deque():
    d = deque()
    #add to right
    d.extend(xrange(4,8))
    print "extend:",d
    d.append(89)
    print "append:",d

    #add to left
    d.extendleft('happy')
    print "extendleft:",d
    d.appendleft('new year')
    print "appendleft:",d

    print "d[3]:",d[3]
    del d[3]
    print "after del d[3]:",d
    d.remove(89)
    print "remove 89:",d

#双端队列线程安全
def burn(decrtion, pdeque):
    while True:
        try:
           item = pdeque()
        except IndexError:
            break
        else:
            print "%s: %s\n"%(decrtion, item)
        time.sleep(0.1)
    print "%8s done"%decrtion
    return


def deque_func():
    de = deque('hapnwyar')
    left = threading.Thread(target=burn, args=('left',de.popleft))
    right = threading.Thread(target=burn, args=('right', de.pop))

    left.start()
    right.start()

    left.join()
    right.join()

#双端队列  旋转
def de_rotate():
    de = deque(xrange(10))
    print "Nomal:",de
    de.rotate(2)
    print "right rotate:",de

    de = deque(xrange(10))
    de.rotate(-2)
    print "left rotate:",de


#namedtuple
def init_nt():
    t = namedtuple('Person', 'name age sex major')
    print 't:',t
    p = t(name='Bob', age='40', sex='Man', major='computer')
    print 'p:',p
    print "%s %s %s %s"%p


#ordereddict  会记住元素插入的顺序  比较两个字典相等时会比普通字典多比较元素插入的顺序
def init_od():
    d={}
    d['1'] = 'a'
    d['2'] = 'b'
    d['3'] = 'c'
    print "dict:",d
    for key,value in d.items():
        print key,value

    od = OrderedDict()
    od['1'] = 'a'
    od['2'] = 'b'
    od['3'] = 'c'
    print "ordereddict:",od
    for key,value in od.items():
        print key, value

def eq_od():
    d1 = dict(a=1,b=2,c=3)
    d2 = dict(b=2,a=1,c=3)

    od1 = OrderedDict(a=1,b=2,c=3)
    od2 = OrderedDict(b=2, a=2, c=3)

    print "dict:",d1==d2
    print "OrderedDict:",od1==od2

if __name__ == '__main__':
    # init()
    # oper_counter()
    #
    # print "=========defaultdict========="
    # init_d()
    #
    # print "=========deque================"
    # init_deque()
    # deque_func()
    # de_rotate()

    print "==========namedtuple=============="
    init_nt()

    print "===========Ordereddict============="
    init_od()
    eq_od()