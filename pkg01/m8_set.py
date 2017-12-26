# coding=utf-8
# pylint: disable=invalid-name
'''
set
'''
s1 = set(["qqq", "aa"])
print s1
s2 = set("abcd")
print s2
s3 = {1, 2, 3, ''}
print s3
s3 = set({1, 2, 3})
print "s3: ", s3
# add
print s3.add(122)
print s3.add("AB")
s3.add(None)
print s3
# update
s4 = {1, 2, 3, 4}
s4.update({11, 222})
print s4
# remove 删除指定的元素
print s4.remove(11)
print s4
# pop 随机删除一个元素
print s4.pop()

# 不可变集合
s4 = frozenset({1, 2, 3})
print s4
s4 = frozenset("ABC")
print s4
s4 = frozenset([1, 2, 3])
print s4

print '=========集合运算======================='
s5 = {"a", "b", "c", "f"}
print "a" in s5
s6 = {"a", "c", "b", "e"}
print s5 == s6
print s5 < s6

print s5 | s6
print s5 & s6
print s5 - s6
print (s5 - s6) | (s6 - s5)
