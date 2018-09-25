'''
common module
'''
import math
PI = math.pi
E = math.e

def __func():
    "func"
    cache = {}
    def temp(name):
        "temp"
        if cache.has_key(name):
            return cache[name]
        else:
            cache[name] = "cache_" + name
            return "cache"
    return temp

mainf = __func()

# print __name__
# print __file__
# print __import__
# print __package__
# print __doc__
print __name__
