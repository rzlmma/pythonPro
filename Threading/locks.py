# -*- coding:utf-8 -*-
from threading import *
import time

b = 90
l = Lock()


def thread_code():
    global b
    print"thread %s invoked"%(currentThread().getName())
    l.acquire()
    try:
        print "thread %s running"%(currentThread().getName())
        b = b + 50
        time.sleep(1)
        print "thread %s set b to %d"%(currentThread().getName(), b)
    finally:
        l.release()

childThreads = []

for i in range(1,5):
    t = Thread(target=thread_code, name='thread_%d'%(i))
    t.setDaemon(1)
    t.start()
    childThreads.append(t)

for item in childThreads:
    item.join()

print "value of b:",b
