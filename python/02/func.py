'''
function
'''
# import list0
# from list0 import data

def calc(count, *args):
    print type(args)
    print args
    return count



print calc(100, [1, 2, 3])

tu = ({'a': 100}, 2)
tu[0]['a'] = 200
print tu

# def f(n123):
#     if n123 == 0 or n123 == 1:
#         return 1
#     return n123 * f(n123 -1)
# print f(5)

# def f2(): 
#     return f

# print f2()(3)

# sum = lambda a, b : a * b

# print sum(1212112, 23)

# print data
