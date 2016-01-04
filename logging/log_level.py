# -*- coding:utf-8 -*-
"""
日志级别：
CRITICAL 50
ERROR    40
WARNING  30
INFO     20
DEBUG    10
只有大于日志记录器和处理器设置的日志级别的日志消息才会发布出来
"""
import logging,sys
LOG_LEVEL={
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}


level_name = sys.argv[1] if len(sys.argv)>1 else 'unset'
logging.basicConfig(level=LOG_LEVEL.get(level_name, logging.NOTSET),
                    )

logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is a error message')
logging.critical('this is a critical message')