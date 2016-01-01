# -*- coding:utf-8 -*-
"""
挑选出文件中某个日期之后创建的所有文件，根据文件的创建时间来判断
"""
import os,datetime

class classifyFile(object):
    def __init__(self, compareTime, dirpath):
        self.compareTime = compareTime
        self.dirpath = dirpath

    def fileLaterThan(self):
        print "比较时间:",self.compareTime
        fileInfo ={}
        rest = []
        for dirname,dirs,files in os.walk(self.dirpath):
            for item in files:
                file_ctime = datetime.datetime.fromtimestamp(os.path.getctime(item))
                print "文件名:%s   文件创建时间:%s"%(item,file_ctime)
                if file_ctime > self.compareTime:
                    rest.append(item)
            fileInfo[dirname] = rest
        return fileInfo

    #过滤出py or html 文件
    def filterFiles(self,*pattern):
        fileSet = {}
        rest = []
        for dirname, dirs,files in os.walk(self.dirpath):
            for file in files:
                items = file.split('.')
                if items[1] in pattern:
                    rest.append(file)
            fileSet[dirname] = rest
        return fileSet



if __name__ == "__main__":
    dirs = os.getcwd()
    print "当前工作目录:",dirs
    compareTime = datetime.datetime(2015,1,1,10,0)
    file_classify = classifyFile(compareTime,dirs)
    files = file_classify.fileLaterThan()
    for item in files.items():
        print "dirname:%s  filename:%s"%(item[0],item[1])

    print file_classify.filterFiles('py','html')