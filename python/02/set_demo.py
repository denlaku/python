s1 = set("hello")
s2 = set(['e', 'K'])
print s1
print s2.issubset(s1)

print s1 | s2
print s1 & s2
print s1 - s2  

# s1 = set("hello")
# data = ["hello", "hello"]
# s1 = set(data)
# s1.add(100)
# s1.add(())
# s1.add(())

# s2 = {"1", 1, 2, 1}  不提倡这种创建集合的方式

# s2 = set(['a', 'b'])
# s1.update(s2)
# s1.update(['a', 'b'])
# s1.update((1, 2, 3))
# s2.update({'aaa': 111})

# print s1
# print 100 in s1
# # print s2