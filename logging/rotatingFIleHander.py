# -*- coding:utf-8 -*-
"""
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size.
"""
import logging
from logging import handlers

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)
handler = handlers.RotatingFileHandler(
                             filename='mylogger.txt',
                             maxBytes=20,
                             backupCount=5,
)

fmt = logging.Formatter('%(asctime)s - %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
handler.setFormatter(fmt)
my_logger.addHandler(handler)
my_logger.debug('this is a debug message')
my_logger.info('this is a info message')
my_logger.warning('this is a warning message')
my_logger.error('this is a error message')