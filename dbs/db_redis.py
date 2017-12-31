# coding=UTF-8
# pylint: disable=invalid-name
'''
redis
'''
import redis

r = redis.Redis('localhost', 6379, 0)
r.set('BB', 200)
print(r.get('AA'))
print(r.keys())
