# coding=utf-8
# pylint: disable=invalid-name
'''
元组: 其中的元素不能更改，元素可以是任何类型的数据
'''
t1 = () # 空元组
print t1
t2 = (1, ) # 只有一个元素的元组，逗号是必须的
print t2
t2 = (1, 2, 3, 4, 5, 6, 7)
print t2
print t2[0] # 索引
print t2[1: 3] # 切片，生成一个新的元组
print t2.count(1)
print t2.index(4)
