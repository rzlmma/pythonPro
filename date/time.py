# -*- coding:utf-8 -*-
"""
datetime
执行复杂的时间计算 python-dateutil
得到与时区相关的日期  pytz
"""
from datetime import timedelta,datetime,date
import calendar
#表示时间段
a = timedelta(days=2, hours=3)
print a

#表示指定的日期和时间
time = datetime(2016,1,6,14,6)
print "time:",time
print "timedelta:", time+a

start_day = date.today().replace(day=1)
print "start_day:",start_day
weekday,days_in_month = calendar.monthrange(start_day.year,start_day.month)
print "weekday:",weekday
print  "days_in_month", days_in_month
end_day = start_day + timedelta(days=days_in_month)
print "end_day:",end_day


#python中的日期和时间可以用标准的数学运算来计算
def date_range(start,stop,offest):
    while start < stop:
        yield start
        start += timedelta(hours=offest)

for time in date_range(datetime(2016,1,1),datetime(2016,1,7),12):
    print "time:",time

#字符串转换为日期
time = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
print "time:%s  type:%s"%(time,type(time))
text = '2016/1/6'
date = datetime.strptime(text,'%Y/%m/%d')         #性能太差，如果要解析大量的日期文本，可以自己实现解析函数
print "date:",date