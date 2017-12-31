# coding=UTF-8
# pylint: disable=invalid-name
'''
yaml
'''
import yaml

f = open('pkg04/test.yaml')
x = yaml.load(f)

print(x)

print("------------------------")
