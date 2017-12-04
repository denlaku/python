# coding=UTF-8
# pylint: disable=invalid-name
'''
列表
'''
alist = [1, '2', 'GG']
print alist

print alist[0]
print alist[-1]
# print list(reversed(alist))
# print alist.reverse()
print alist
# len函数获取list的长度
print len(alist)
# 用+号连接两个list
print [1, 2] + ["a", "b"]
# *, 重复元素
print alist * 2
# in，判断是否在list中
print 1 in alist
# max 和 min 函数
print max(alist)
print min(alist)

print '-----------------------列表的函数-------------------------'
tmp = []
# 追加元素
tmp.append(100)
print tmp
# extend 合并两个列表
T1 = [100, 'QAA']
T2 = [111, 222, 333]
T1.extend(T2)
print T1
# extend还可以吧字符串加入列表，字符串被拆解成了一个一个的字符
T1.extend("MOPPPPPP")
T1.extend('') # 如果添加的字符串为空, 则列表不会有变化
print T1
# count 统计指定元素在list中出现了多少次
print T1.count('P') # 6次
# index 返回执行元素在列表中第一次出现的下标。如果list中不存在指定元素，就会报错。所以最好先用in判断执行元素是否在list中
if 'p' in T1:
    print T1.index("P")
else:
    print "列表T1中不存在元素p"
