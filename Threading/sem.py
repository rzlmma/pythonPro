# -*- coding:utf-8 -*-
"""
semaphore（旗语）管理访问有限的资源
"""
import threading
import time, random


def number_gen(sem, queue, qlock):
    while True:
        time.sleep(2)
        value = random.randint(1,100)
        qlock.acquire()
        try:
            queue.append(value)
        finally:
            qlock.release()
        print "thread %s append value %d to queue"%(threading.currentThread().getName(), value)
        sem.release()


def number_cal(sem, queue, qlock):
    while True:
        time.sleep(5)
        sem.acquire()
        qlock.acquire()
        try:
            value = queue.pop()
        finally:
            qlock.release()
        print "thread %s pop value %d from the queue"%(threading.currentThread().getName(), value)


sem = threading.Semaphore()
qlock = threading.Lock()
queue = []
childthreads = []

t = threading.Thread(target=number_gen, args=(sem, queue, qlock))
t.start()
childthreads.append(t)

for i in range(1,3):
    w = threading.Thread(target=number_cal, args=(sem, queue, qlock))
    w.start()
    childthreads.append(w)

time.sleep(300)

