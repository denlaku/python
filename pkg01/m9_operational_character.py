# coding=UTF-8
# pylint: disable=invalid-name
'''
运算符
'''
from math import sqrt
print(1e4)
print(1.3454545e4)
print(10 ** 4)
print(10 / 3.0)
print(10 // 3.0) # 返回商的整数部分

a = 100
if a < 50:
    print("<50")
elif a < 100:
    print("<100")
else:
    print('>=100')

# 三元操作符
# A = Y if X else Z
name = "a123" if a else 'b456'
print("name:", name)

print('---------------------for---------------------')
# 循环语句
for a in range(1, -100, -1): # range(start, stop, step) 不包含stop,stop是必须的,step默认为1,一定不能为0
    if not a % 33:
        print("range:", a)
for a in [1, 2]: # 循环列表
    print(a)
for a in ('n', 'GK'): #循环元组
    print(a)
for a in {'aa': 100, 'bb': 200}: # 循环字典
    print("dict:", a)
for a in "AB": # 循环字符串
    print(a)
nums = [2, 3, 4]
print([x * x for x in nums])
# print ({'aa': 100, 'bb': 200}).items()
for a in range(6, 9):
    r = sqrt(a)
    if r == int(r):
        print(r)
        break
else:
    print('nothing')

print('---------------------while---------------------')
i = 3
while i > 0:
    print('while:', i)
    i -= 1

k = 3
while k > 10:
    print('while else: ', k)
    k -= 1
    if k <= 0:
        break
else:
    print('end while else', k)

print('-----end-----')
