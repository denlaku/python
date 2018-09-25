#!/usr/bin/env python
# coding=UTF-8
t = True
a = 100
s = u'Python编程语言'
# while t:
#     if (a - 33) == 0:
#         t = False
#     a = a - 1
#     print a


# for c in s:
#     print c

# for c in range(5):
#     print c

list0 = [1, '2', '---']
for l in list0:
    print l

for i, item in enumerate(list0):
    print i, ',', item

dict0 = {
    0: 100,
    'c': 200,
    (1, 2, 3): 300,
    None: 400
}

for key in dict0:
    print key, dict0[key]
