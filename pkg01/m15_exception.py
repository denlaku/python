# coding=UTF-8
# pylint: disable=invalid-name
'''
异常
'''
a = 1

try:
    i = 10 / a
    print("a: ", a)
except ZeroDivisionError:
    print("the second num can't be zero!")
else:
    print("try-else") # try中没有出现任何异常，才会执行else
finally:
    print("finally")

# assert 1 == 2
assert 1 != 2
print("--------end-----------")
