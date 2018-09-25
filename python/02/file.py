'''
file
'''
import os
import time

stat = os.stat('temp.txt')
print stat
print stat.st_mode
ct = time.localtime(stat.st_ctime)
print ct
print ct.tm_year
print ct.tm_mon
print ct.tm_mday
print ct.tm_hour
print ct.tm_min
print ct.tm_sec

# with open('https://github.com/denlaku', 'r') as g:
#     pass

# with open('temp.txt', 'a') as tmp:
#     tmp.writelines('DDDDDD\n')
#     # print tmp.readline()
# i = 0
# with file('temp.txt', 'r') as tmp:
#     for line in tmp:
#         i = i + 1
#         print i, line.strip()
