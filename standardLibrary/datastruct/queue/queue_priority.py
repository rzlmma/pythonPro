# -*- coding:utf-8 -*-
"""
优先队列
"""
import Queue, threading
class Job:
    def __init__(self, priority, decrition):
        self.priority = priority
        self.decrition = decrition
        print "New Job: %s %s"%(self.priority, self.decrition)

    def __cmp__(self, other):
        return cmp(self.priority, other.priority)

q = Queue.PriorityQueue()
q.put(Job(3, 'Middle-level Job'))
q.put(Job(6, 'Middle-level Job'))
q.put(Job(10, 'Last-level Job'))
q.put(Job(1, 'Import-level Job'))

def process_job(q):
    while True:
        job = q.get()
        print "process job:",job.decrition
        q.task_done()

workers = [threading.Thread(target=process_job, args=(q,)),
           threading.Thread(target=process_job, args=(q,))
           ]

for w in workers:
    w.setDaemon(True)
    w.start()

q.join()