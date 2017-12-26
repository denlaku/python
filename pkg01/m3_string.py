# coding=utf-8
# pylint: disable=invalid-name
'''
字符串：由零个或多个字符组成的有限串儿
'''
S1 = 'absc'
print S1

S2 = "uuuuuu"
print S2

S3 = """start
`
1
23
end"""
print S3

# 连接字符串
print S1 + S2

A = 1000
# print 'money: ' + A   报错
# 用 + 拼接的两个对象必须是同一种类型

print `A` # 反引号可以将对象转换为字符串，但是不建议使用
# str函数： 将对象转换为字符串
print 'money: ' + str(A)

print type(A)
print type("")
print isinstance('', float)
# 转义字符
print '\''
print "\""
print '\\'
num = '''1111'''
print num

str1 = "abcdefg"
print str1.index('c')
print len(str1)
print cmp(str1, str1)
print str1.replace('A', '电放费')

arr = ['1', 'A', "3"]
print "".join(arr)

# 字符串格式化输出
print '%s ddff' % '替代'

print "======================part2=================="
s = 'abcdefghijklmn'
print s[1:5] # 截取字符串

print s.split('f')
