# -*- coding:utf-8 -*-
# __author__ = majing
"""
时间处理类
"""
import datetime


class DateTimeHelper(object):

    format_d = ['%Y', '%m', '%d']
    format_t = ['%H', '%M', '%S']

    @classmethod
    def gen_str_format(cls, is_second=False, d_split="-", t_split=":"):
        """
        :param is_second: 是否显示秒数
        :param d_split:   日期分隔符
        :param t_split:   时间分隔符
        """
        first = '%s'.join(cls.format_d) % d_split
        format_t = cls.format_t if is_second else cls.format_t[0:2]
        second = '%s'.join(format_t) % t_split

        return "%s  %s" % (first, second)

    @classmethod
    def current_now(cls, zone=None):
        if zone == 'utc':
            return datetime.datetime.utcnow()
        return datetime.datetime.now()

    @classmethod
    def utc_to_current(cls, val):
        """
        把utc时间转换程当前时间
        """
        pass

    @classmethod
    def timedelta_to_seconds(cls, t1, t2, _format=None):
        """
        2个时间差转换成秒
        _format: t1,t2 为str时的，格式
        """
        if not _format:
            _format = cls.gen_str_format()     # '%Y-%m-%d %H:%M'

        if not isinstance(t1, str):
            t1 = datetime.datetime.strptime(t1, _format)
        if not isinstance(t2, str):
            t2 = datetime.datetime.strptime(t1, _format)
        differ = t1 - t2
        return differ.total_seconds()

    @classmethod
    def datetime_to_str(cls, val, _format=None):
        if not _format:
            _format = cls.gen_str_format()

        if isinstance(val, str):
            return val
        return datetime.datetime.strftime(val, _format)

    @classmethod
    def str_to_datetime(cls, val, _format=None):
        """
        日期字符串转换成datetime.datetime
        :param val: 
        :param _format: 
        """
        if not _format:
            _format = cls.gen_str_format()
        return datetime.datetime.strptime(val, _format)

    @classmethod
    def timestamp_to_datetime(cls, val, seconds=True, zone=None):
        """
        时间戳转时间
        :param val: 注意val的单位 前端返回的是一毫秒为单位，后端是以秒为单位
        :param seconds: True 以秒为单位
        :param zone: 返回utc时间还是本地时间
        """
        if not isinstance(val, (int, float)):
            val = int(val)

        if not seconds:
            val = val/1000

        if zone == 'utc':
            return datetime.datetime.utcfromtimestamp(val)
        return datetime.datetime.fromtimestamp(val)

    @classmethod
    def datetime_to_timestamp(cls, val):
        """
        时间转时间戳
        :param val: 
        """
        if isinstance(val, str):
            val = cls.str_to_datetime(val)
        return datetime.datetime.timestamp(val)





