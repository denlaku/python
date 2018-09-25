# -*- coding: UTF-8 -*- 

import os
# str = raw_input("请输入：")
# print "你输入的内容是: ", str

f = open('temp.txt', 'r+')
# print f.read(20)
# print f.read(3)
# print f.tell()
f.seek(3)
f.truncate()
# print f.next()
# print f.next()
# print f.next()
# print f.fileno()
# print f.isatty()
# print f.encoding
# print f.mode
# print f.name
# print f.readline()
# print f.newlines
# print f.readlines(10)

# for e in f.readlines(10):
#     print e

# f = open('temp.txt', 'a+')
# f.writelines('这是什么')
# f.write('这是什么')
# f.flush()
# f.close()

# os.rename('temp.txt', 'temp2.txt')
