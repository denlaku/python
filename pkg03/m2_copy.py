# coding=UTF-8
# pylint: disable=invalid-name
'''
copy
'''
import copy

dic = {
    "name": "tom",
}

# 浅复制
new_dic = copy.copy(dic)

# 深度复制
deep_dic = copy.deepcopy(dic)

print(dic == new_dic)
print(dic == deep_dic)
print(new_dic)

if __name__ == "__main__":
    print("--------------------")
