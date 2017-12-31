# coding=UTF-8
# pylint: disable=invalid-name
'''
文件

打开文件模式
r 以读的方式打开文件。****如果文件不存在，则报错。
w 以写的方式打开文件，可想文件写入信息。如果文件不存在，则创建文件，再写入内容。
a 以追加的模式打开文件，文件指针自动移到末尾，如果文件不存在则创建文件。
r+ 以读写的方式打开文件，可以对文件进行读和写。如果文件不存在，则报错。
w+ 消除文件内容，然后以读写的方式打开文件。****如果文件不存在，则创建文件。
a+ 以读写的方式打开文件，并把文件指针移到末尾。如果文件不存在，则创建文件。
b 以二进制模式打开文件，而不是以文本模式

用with的方式操作文件，不用手动去close文件
with open('pkg01/k_07.txt', "w") as f07:
    f07.writelines("this is first line")

'''
import fileinput

# read 如果指定了参数size，则读取size个字符；如果没有指定参数size，则读取所有内容。
with open('pkg01/k_01.txt') as f01:
    print(f01.read(7))

# readline 如果没有指定参数size，则默认读取一行。如果指定了参数size，则读取一行中size个字符
with open('pkg01/k_01.txt') as f01:
    print(f01.readline(21))
    print("seek: ", f01.tell())

# readlines 读取所有的行，并以list的形式返回
with open('pkg01/k_01.txt') as f01:
    print(f01.readlines())

# 报错
# with fileinput.input('pkg01/k_01.txt') as f01:
#     print f01.readlines()

for line in fileinput.input('pkg01/k_01.txt'):
    print(line)


# f01 = open('pkg01/k_01.txt')
# for line in f01:
#     print line.strip()

# print '---open file by with---'
# with open('pkg01/k_01.txt') as f01:
#     for line in f01:
#         print line.strip()

# gitfile = open("https://github.com/denlaku", "r")

# print '----创建文件-----'
# f02 = open('pkg01/k_02.txt', 'w')
# f02.writelines("first line")
# f02.write('111')
# f02.flush()

# f02 = open('pkg01/k_03.txt', 'w+')
# f02.flush()

# f04 = open('pkg01/k_04.txt', 'r+')
# f04.flush()

# f05 = open('pkg01/k_05.txt', 'a')
# f05.flush()

# f06 = open('pkg01/k_06.txt', 'a+')
# f06.flush()

# with open('pkg01/k_07.txt', "w") as f07:
#     f07.writelines("this is first line")


print('----------------end-------------')
