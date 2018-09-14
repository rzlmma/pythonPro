# -*- coding:utf-8 -*-
"""
把log信息输出到一个文件中
具体可参考blog:http://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
"""
import logging, sys

logging.basicConfig(
            level=logging.DEBUG,
            filename='log.txt',
            filemode='w',
            datefmt='%Y-%m-%d %H:%M:%S',
            format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
)


logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')



print("--------log.txt--------")
for line in open('log.txt'):
    print(line)

