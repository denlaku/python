# coding=UTF-8
# pylint: disable=invalid-name
'''
class
'''
class AA:
    inner = "IIIIII"
    pass

aa = AA()
aa.id = 100
print(type(AA))
print(type(aa))
print(aa.__class__)
print(aa.id)
print(aa.inner)

print("===============BB=================")
class BB(object):
    pass
bb = BB()
bb.id = 100
print(bb)
print(type(BB))
print(type(bb))
print(bb.__class__)
print(bb.id)

__metaclass__ = type
class Person:
    X = 100 # 类的属性
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

print("Person.X", Person.X)
p1 = Person("first")
print(p1)
print(p1.getName())
p1.setName("change: tom")
print(p1.getName())
print(Person.__class__)


class Girl(Person):
    def __init__(self, name, color):
        super(Girl, self).__init__(name)
        self.color = color
    def getColor(self):
        return self.color
    def setColor(self, color):
        self.color = color


class classA(object):
    def getName(self):
        print("classA.getName")

class classB(object):
    def getName(self):
        print("classB.getName")

class classC(classA, classB):
    pass

c1 = classC()
c1.getName()


g1 = Girl("GGG", "red")
print(g1.getName())

print('-------------------------------end-------------------------------')
