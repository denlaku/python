# -*- coding: UTF-8 -*-
'''
time and date of python
'''
import time
import math
import calendar

# time.sleep(10)
print time.time()

print math.modf(time.time())

print type((1, 2, 3))

# lt = time.localtime()
# print type(lt)
# print type(lt[0])
# print type('')

# print type(lt[0]) if type(lt[0]) < 2017 else 100

# for i in lt:
#     print i
# lt.

# print time.strftime('%Y-%m-%d %H:%M:%S')

# t = time.time()
# print t
# lt = time.localtime(t)
# print lt

# print time.strftime('%Y-%m-%d %H:%M:%S %A %a %w %W %j %p', lt)

# print time.clock()
# print time.asctime(lt)
# print time.ctime()
# print time.altzone
# print time.mktime((2009, 2, 17, 17, 3, 38, 1, 48, 0))

# cal = calendar.month(2016, 1)
# print "以下输出2016年1月份的日历:"
# print cal

# print time.timezone, time.tzname

# print time.struct_time

# print calendar.isleap(2012)
# print calendar.leapdays(170, 2953)
