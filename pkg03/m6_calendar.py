# coding=UTF-8
# pylint: disable=invalid-name
'''
heapq
'''
import calendar

# 判断闰年
print(calendar.isleap(1900))
# 返回两个年份y1,y2之间闰年的总数,包含y1不包含y2
print(calendar.leapdays(2001, 2015))
# 判断执行日期是星期几
print(calendar.weekday(17, 12, 26))

cal = calendar.calendar(2015)
# print cal

print("--------------------")
month = calendar.month(2015, 2)
print(month)

if __name__ == "__main__":
    print("--------------------")
