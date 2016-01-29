# -*- coding:utf-8 -*-
"""
Queue 先进先出 线程安全
"""
from __future__ import print_function
import Queue, time, threading


def qu_fifo():
    """
    FIFO  先进先出
    :return:
    """
    q = Queue.Queue()
    for i in range(1,6):
        q.put(i)

    while True:
        if q.empty():
            break
        item = q.get()
        print(item, end=' ')

def create_qu(q):
    for i in range(1,6):
        print("put item:%s"%(i))
        q.put(i)
        time.sleep(1)

def cost_qu(q):
    while True:
        if q.empty():
            break
        item = q.get()
        print("get item:%s"%(item))
        time.sleep(1)

def main():
    q = Queue.Queue()
    create = threading.Thread(target=create_qu, args=(q,))
    cost = threading.Thread(target=cost_qu, args=(q,))

    create.start()
    cost.start()

    create.join()
    cost.join()


def qu_lifo():
    """
    LOFO 后进先出
    :return:
    """
    q = Queue.LifoQueue()
    for i in range(1,6):
        q.put(i)

    while True:
        if q.empty():
            break
        item = q.get()
        print(item, end=' ')


if __name__ == '__main__':
    print("============FIFO===========")
    qu_fifo()
    print()
    main()
    print("=============LIFO===========")
    qu_lifo()