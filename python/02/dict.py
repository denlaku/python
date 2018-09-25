org = {
    'class': 'Tom',
    'name': '||||||'
}

org2 = {
    'name': 'Tom'
}

person = {
    'name': 'Jeck',
    'age': 100,
    'isMan': True,
    100: 10001,
    # (1, 2, 3): 123,
    True: False
}

print person.get('name123')

# print person.pop('name1', None)
print person.popitem()
print person.popitem()
print person

# print person.update(org)
# print person

# print person.values()

# print person.setdefault('aaaa', '---')
# print person.setdefault('name', '+++')
# print person

# print dict.fromkeys({'age': 100, 100: 200})
# print dict.fromkeys((1,2,3,4), 100)
# print dict.fromkeys([11, 22, 33], 'test')
# print person.items()
# for p in person.items():
#     print p[0], p[1]

# print person
# print person['name']
# print person[(1, 2, 3)]
# print person[100]
# print person[True]
# del person[100]

# print len(person)
# person.clear()
# print len(person)
# print str(person)
# print type(person)

# per = person.copy()
# print per.get('org') == person.get('org')
# print per.get('org') == org.copy()
# print per == org2
# print org == org.copy()

# orgcopy = org.copy()
# orgcopy['age'] = 100
# print orgcopy
# print org
# print orgcopy == org

# print person
