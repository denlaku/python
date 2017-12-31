# coding=UTF-8
# pylint: disable=invalid-name
'''
函数
'''

def add(a, b=7, c=5):
    return a + b + c

print(add(1, 10))


def fibs(n):
    if n < 2:
        return n
    return fibs(n-2) + fibs(n-1)

print(fibs(12))

def morearg(*args):
    print(type(args)) # 元组
    print(args)

morearg("", 1)
morearg(*(1, 2))

def morearg2(**args):
    print(type(args)) # 元组
    print(args)
morearg2(a=10, b=20)
morearg2(**{"a": 100})

lam = lambda x, y=100: x + y
print(lam(10))

print("----------map--------------")
print(map(lambda x: x**2, [5, 3, 2]))
print(map(lambda x, y: x*y, [5, 2, 3], [11, 12, 1]))

# map/filter on lambda could be replaced by comprehension
print([x ** 2 for x in [5, 3, 2]])
print([x * y for x in [5, 2, 3] for y in [11, 12, 1]])

print("----------reduce--------------")
print(reduce(lambda x, y: x + y, [1, 2, 3]))

print("----------filter--------------")
print(filter(lambda x: x > 300, [100, 222, 0]))

# print __name__, __file__, __debug__

print('-------------------end---------------------')
