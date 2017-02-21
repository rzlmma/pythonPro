# -*- coding:utf-8 -*-
"""子类化Thread类"""
import threading, time
loops = [4, 2]


class MyThread(threading.Thread):
    def __init__(self, index, sec):
        super(MyThread, self).__init__(self)
        self.index = index
        self.sec = sec

    def run(self):
        print "loop starts:%d"%(self.index) + "  %s\n"%(time.ctime())
        time.sleep(self.sec)
        print "loop ends:%d"%(self.sec) + "  %s\n"%(time.ctime())


def main():
    nloop = range(len(loops))
    threads = []
    for i in nloop:
        tt = MyThread(i,loops[i])
        print "线程名字：",tt.getName()
        threads.append(tt)
    for i in range(len(loops)):
        threads[i].start()

    for item in threads:
        item.join()

    print "all done:%s\n"%(time.ctime())
      
      
if __name__ == "__main__":
    main()