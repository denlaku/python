# coding=UTF-8
# pylint: disable=invalid-name
'''
deque
'''
# from collections import deque
import collections
from collections import deque
print collections.__all__

l0 = [1, 2, 3]
ql0 = deque(l0)
ql0.appendleft(11)
print ql0

if __name__ == "__main__":
    print "--------------------"
