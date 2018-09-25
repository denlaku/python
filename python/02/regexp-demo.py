import re

# result = re.match('(\w*)\d+(\w*)$', '-GD12434U')

# print result

# if result:
#     print result.group()
#     print result.groups()
#     print result.span()
# else:
#     print 'No match!'

# r1 = re.match('^(?!dg)', 'deg')
# if r1:
#     print r1.group()
# else:
#     print 'No match!'


# r2 = re.match('dg\d+', 'KKdg2323')
# if r2:
#     print r2.group()

# print  're.IGNORECASE: %d' % (re.I)
# print  're.IGNORECASE: %d' % (re.IGNORECASE)
# print  're.LOCALE: %d' % (re.L)
# print  're.LOCALE: %d' % (re.LOCALE)
# print  're.MULTILINE: %d' % (re.M)
# print  're.MULTILINE: %d' % (re.MULTILINE)
# print  're.S: %d' % (re.S)
# print  're.UNICODE: %d' % (re.U)
# print  're.UNICODE: %d' % (re.UNICODE)
# print  're.X: %d' % (re.X)
# s1 = '3Abcg'
# print s1
# print re.sub('3a', 'QQ', s1, 0, re.I | re.L)
# print s1

s2 = 'month,year,day,minute,second,hour'
print re.split(',', s2, 0, re.I)