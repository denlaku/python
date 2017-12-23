# coding=UTF-8
# pylint: disable=invalid-name
'''
copy
'''
import copy

dic = {
    "name": "tom",
}

new_dic = copy.copy(dic)

deep_dic = copy.deepcopy(dic)

print dic == new_dic
print dic == deep_dic
print new_dic

print "--------------------------------"
