# coding=utf-8
# pylint: disable=invalid-name
'''
字典：存储的是键值对 key: value;key是惟一的，不能重复;
key是不可变的，如字符串、数字等固定的值，也可以是元组；列表是可变的，不能作为key
'''
import copy
mydict = {} #创建字典
person = {"name": "tom", "site": "github", 'del': "delete", "arr": [0, '1']} # 创建一个不为空的字典
print person
print person['name']
site = "site"
print person[site]
person[site] = 10000 # 向字典添加键值对
print person
l1 = ''
person[l1] = 1000
person[(1,)] = 'tup'
print person
print person[(1,)]

# len 返回字典中键值对的数量
print len(person)
# del 删除字典里的key, 如果指定的key不存在则报错
del person['del']
print person
# 检查字典中是否存在指定的key
print 'del' in person
print '' in person

# copy 拷贝字典
print '===========copy==========='
# copyPerson = person.copy()
copyPerson = copy.deepcopy(person)
print copyPerson
print copyPerson == person
print id(copyPerson), id(person)
print id(copyPerson['arr']), id(person['arr'])

# 利用字典格式化字符串
sen = '%(name)s 是一个很好的人, 年龄: %(age)s'
tmpsen = sen % {"name": "Jeck", "age": 28}
print tmpsen

obj = {"name": "obj-name", "key": "k1", 'none': None, 'true': True}
# get 获取指定key的值。如果key存在则返回key对应的value， 如果key不存在怎返回None;可以指定第二参数， 如果key不存在，则返回值为第二个参数
print obj.get("name1", "true")
# setdefault 设置键值对。若果指定的key存在，则返回key的value，如果key不存在，则在字典添加key，value为第二个参数，如果没有指定第二参数，则value为None
print obj.setdefault('name')
print obj
print '===========================items=========================='
stu = {"name": "my-name", "address": "my-address", "site": "my-site"}
print stu.items() # 得到一个关于字典的列表，列表中的元素是字典的键值组成的元组
print list(stu.iteritems())
print stu.keys()
print stu.values()
# 删除字典中指定的key
print stu.pop('name')
print stu
# 随机删除key
print stu.popitem()
print stu
print '===========================update=========================='
per = {"name": "my-name", "address": "my-address", "site": "my-site"}
per.update({"name": "kk-val"})
print per
print per.has_key('name')
