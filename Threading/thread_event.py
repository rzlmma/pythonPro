# -*- coding:utf-8 -*-
# Copyright (c) 2016 MagicStack

"""
线程事件
"""

from threading import Thread, Event


class MyThread(Thread):
    def __init__(self, sec, event):
        super(MyThread, self).__init__()
        self.sec = sec
        self.event = event

    def run(self, *args, **kwargs):
        if self.event.isSet():
            print "event true:      begin to sleep %s seconds....\n" % self.sec
            self.event.clear()
        else:
            self.event.set()
            print " set event to true......      thread %s" % self.sec


if __name__ == "__main__":
    event = Event()
    threads = []
    for i in range(1, 5):
        t = MyThread(i, event)
        threads.append(t)

    print "The Main Thread"
    for t in threads:
        t.start()

