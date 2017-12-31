# coding=UTF-8
# pylint: disable=invalid-name
'''
iter
'''

class MyRange(object):
    '''1'''
    def __init__(self, n):
        self.i = 0
        self.n = n
    def __iter__(self):
        return self
    def __next__(self): # python3.0以后用__next__方法代替next方法
        '''method'''
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

rg = MyRange(10)

# print(rg.__next__())
# print(rg.__next__())
# print(rg.__next__())
# print(rg.__next__())
# print(rg.__next__())
# print(rg.__next__())

for i in rg:
    print(i)

print("-----------------end----------------")
