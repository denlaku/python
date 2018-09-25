class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
p = Person('tom', 20)


p.name = 1000

print p.name