# coding=UTF-8
# pylint: disable=invalid-name
'''
yaml
'''
import yaml

class Person(object):
    '''
    Person
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("name1", 20)
p2 = Person("name2", 21)
p3 = Person("name3", 22)

persons = [p1, p2, p3]

print yaml.dump(persons)

print "------------------------"
