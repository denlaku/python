# coding=UTF-8
# pylint: disable=invalid-name
'''
url lib
'''
import urllib
baidu = urllib.urlopen("https://www.baidu.com/")
print baidu.read()


if __name__ == "__main__":
    print "--------------------"
