# -*- coding:utf-8 -*-

import threading
import time,sys

def sleepandprint():
    time.sleep(1)
    print "hello from both of us"


def threadcode():
    sys.stdout.write('hello from the new thread. my name is %s\n'%(threading.currentThread().getName()))
    sleepandprint()

print "before starting a new threading. my name is %s\n"%(threading.currentThread().getName())

t = threading.Thread(target=threadcode, name='ChildThread')
t.setDaemon(1)
t.start()

sys.stdout.write('hello from the main thread. my name is %s\n'%(threading.currentThread().getName()))

sleepandprint()

t.join()

