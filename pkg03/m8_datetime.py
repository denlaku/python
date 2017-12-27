# coding=UTF-8
# pylint: disable=invalid-name
'''
datetime
'''
import datetime

print datetime.datetime.now()

today = datetime.date.today()
print today
print today.ctime()
print today.timetuple()
print today.year, today.month, today.day
print datetime.date(2015, 2, 5)

if __name__ == "__main__":
    print "--------------------"
