#coding=utf-8
import time, threading
loops=[4,2]

class MyThread(object):
      def __init__(self, func, args,name=""):
          self.args = args
          self.func = func
          self.name = name

      def __call__(self, *args, **kwargs):
          self.func(*self.args)

def loop(nloop, nsec):
    print "loop starts:%d"%(nloop) + "  %s\n"%(time.ctime())
    time.sleep(nsec)
    print "loop ends:%d"%(nloop) + "  %s\n"%(time.ctime())

def main():
    threads =[]
    for i in range(len(loops)):
        tt = threading.Thread(target=MyThread(loop, (i,loops[i]),loop.__name__))
        print "线程名字：",tt.getName()
        threads.append(tt)
    for i in range(len(loops)):
        threads[i].start()

    for item in threads:
        item.join()

    print "all done:%s\n"%(time.ctime())

if __name__ == "__main__":
    main()
