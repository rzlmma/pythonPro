# -*- coding:utf-8 -*-

from threading import Thread
import time

class CountDownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self,n):
        while self._running and n>0:
            print "item:",n
            n = n -1
            # time.sleep(0.1)

obj = CountDownTask()
t = Thread(target=obj.run, args=(8,))
t.start()
obj.terminate()
t.join()
