# coding=UTF-8
# pylint: disable=invalid-name
'''
sys
'''

import sys
import os

print("file name is: ", sys.argv[0])
print(sys.path)
print(sys.path[0])
print(os.path.split(os.path.realpath(__file__)))

if __name__ == "__main__":
    print ("--------------------")
