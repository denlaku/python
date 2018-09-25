#!/usr/bin/env python
# coding=UTF-8
str = 'Python'
print str
print str[1:3]

print 'P' in str
print 'K' not in str

for c in str:
    print c

# 字符串的格式化
print 'python %d -- %s' % (100, 'abc')
print '121212 {1} sdfsd{3} {2}'.format(1, 3, 4, '--')
print str * 2
