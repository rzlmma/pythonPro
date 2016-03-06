# -*- coding:utf-8 -*-

from threading import Thread, currentThread, enumerate
import time
import logging, random

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


def func():
    """
    threading name
    :return:
    """
    logging.basicConfig(level= logging.DEBUG,
                        format='[%(levelname)s]  (%(threadName)-10s)    %(message)s'
                        )

    def worker():
        logging.debug('worker: starting')
        time.sleep(2)
        logging.debug('worker: existing')

    def service():
        logging.debug('service: starting')
        time.sleep(3)
        logging.debug('service: existing')

    threads = []
    t1 = Thread(name='worker', target=worker)
    threads.append(t1)
    t2 = Thread(name='server', target=service)
    threads.append(t2)
    t3 = Thread(target=service)
    threads.append(t3)

    for item in threads:
        item.start()

def func2():
    """
    daemon 守护线程
    :return:
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s     (%(threadName)-10s)         %(message)s]'
                        )
    def daemon():
        logging.debug('daemon: starting')
        time.sleep(2)
        logging.debug('daemon: exsiting')

    def non_daemon():
        logging.debug('non_daemon: starting')
        logging.debug('non_daemon: exsiting')

    d = Thread(target=daemon)
    d.setDaemon(True)

    t = Thread(target=non_daemon)

    d.start()
    t.start()

    d.join(1)
    t.join()


def func3():
    """
    enumerate
    :return:
    """
    logging.basicConfig(level=logging.DEBUG,
                        format='[%(levelname)s]     (%(threadName)-10s)    %(message)s'
                        )
    def worker():
        t = currentThread()
        pause = random.randint(1,5)
        logging.debug('sleeping: %s', pause)
        time.sleep(pause)
        logging.debug('ending')
        return

    for i in range(3):
        t = Thread(target=worker)
        t.setDaemon(True)
        t.start()


    main_thread = currentThread()
    for item in enumerate():
        if item == main_thread:
            continue
        logging.debug('joining  %s'%(item.getName()))
        item.join()






if __name__ == '__main__':

    # obj = CountDownTask()
    # t = Thread(target=obj.run, args=(8,))
    # t.start()
    # obj.terminate()
    # t.join()
    # func()
    # func2()
    func3()