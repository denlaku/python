# -*- coding: UTF-8 -*-
'''
python common
'''
# import common
import common
import math
import lib.java

# print common.PI

print common.PI, common.E

Money = 200
def add_money():
    # print globals()
    # print locals()
    global Money
    Money = Money + 1

print Money
add_money()
print Money

# print dir(math)

# print globals()
# print locals()

# print common.mainf('name')
# print common.mainf('name')
# print common.__func()('asas')

print lib.java.version
