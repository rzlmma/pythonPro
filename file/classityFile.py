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
        if not os.path.exists(self.dirpath):
            raise ValueError('please check the path! path is not exists!!!')
        for dirname,dirs,files in os.walk(self.dirpath):
            for item in files:
                file_ctime = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(dirname,item)))
                print "文件名:%s   文件创建时间:%s"%(item,file_ctime)
                if file_ctime > self.compareTime:
                    rest.append(item)
            fileInfo[dirname] = rest
        return fileInfo

    #过滤出py or html 文件
    def filterFiles(self,*pattern):
        fileSet = {}
        rest = []
        if not os.path.exists(self.dirpath):
            raise ValueError('please check the path! path is not exists!!!')
        for dirname, dirs,files in os.walk(self.dirpath):
            for file in files:
                items = file.split('.')
                if len(items)<2:
                    continue
                if items[1] in pattern:
                    rest.append(file)
            fileSet[dirname] = rest
        return fileSet

    #获取文件的信息：路径，大小，修改时间,返回排序后的文件
    def getFileInfo(self, param):
        fileInfo ={}
        if not os.path.exists(self.dirpath):
            raise ValueError('please check the path! path is not exists!!!')
        for root, dirs, files in os.walk(self.dirpath):
            for item in files:
                file_name = os.path.join(root,item)
                file_size = os.path.getsize(os.path.join(root,item))
                file_mtime = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root,item))).strftime('%Y-%m-%d  %H:%M:%S')
                fileInfo[file_name] = {'file_size': file_size, 'file_mtime': file_mtime}

        fileInfo = sorted(fileInfo.items(), key=lambda x: x[1].get(param, ' '), reverse=False)
        return fileInfo

if __name__ == "__main__":
    dirs = os.getcwd()
    print "当前工作目录:",dirs
    compareTime = datetime.datetime(2015,1,1,10,0)
    file_classify = classifyFile(compareTime, r'f:\pythonPro\pythonPro')

    print "------------在给定时间之后创建的文件--------"
    files = file_classify.fileLaterThan()
    for item in files.items():
        print "dirname:%s  filename:%s"%(item[0],item[1])

    print "---------过滤出py,html文件-------------"
    print file_classify.filterFiles('py','html')

    print "-------排列-------------"
    for item in file_classify.getFileInfo('file_size'):
        print item