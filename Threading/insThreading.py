# -*- coding:utf-8  -*-
"""创建一个threading.Thread的实例，传进一个函数"""
import threading, time

loops=[4,2]  

def func(index, sec):  

      print "func starts:%d"%(index)+"  %s\n"%(time.ctime())  
      
      time.sleep(sec) 
      
      print "func ends:%d"%(index)+"  %s\n"%(time.ctime())  
      
      
def main():  

     threads =[]  
     
     nloop = range(len(loops))
     
     for i in nloop:  
     
          tt = threading.Thread(target=func, args=(i, loops[i]))  
          
          print "the name of the threadind:%s\n"%(tt.getName())  
          
          threads.append(tt)  
    
     for i in nloop:  
     
          threads[i].start()  
  
     for i in nloop: 
     
           threads[i].join()  #允许主线程等待所有的线程运行完之后在执行后面的逻辑  
           
     print "all done:%s\n"%(time.ctime())  
  
if __name__ == "__main__":  

     main()  
