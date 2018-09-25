'''
list
'''

list0 = [1, 4, 5, 2, 3, 0]

del list0[1]

list0.extend(('aa', 'bb'))
list0.extend(['cc', 'dd'])

list0.insert(2, 'insert')
list0.remove(1)

list0.sort()

list0.reverse()

list0.append('abc')

print list0.count(1)

print len(list0)

print list0[2:3]

print list0
