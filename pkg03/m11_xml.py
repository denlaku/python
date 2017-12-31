# coding=UTF-8
# pylint: disable=invalid-name
'''
xml
'''
import xml.etree.cElementTree as ET

tree = ET.ElementTree("pkg03/m11_testxml.xml")
root = tree.getroot()
print(type(root))

if __name__ == "__main__":
    print("--------------------")
