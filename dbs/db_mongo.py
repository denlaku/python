# coding=UTF-8
# pylint: disable=invalid-name
'''
mongodb
'''
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

test = client.test
col = test.col
cols = col.find()

# 查询数据
# for c in cols:
#     print '_id:', c.get('_id')
#     print 'name:', c.get('name')
#     print 'type:', c.get('type')
#     print 'able:', c.get('able')
#     print '--------------------------------'

# 掺入数据
# col.insert({
#     "name": "J-001",
#     "type": "F",
#     "able": True
# })

# 删除数据
# col.remove({"name": "J-001"})

# 修改数据
col.update({"name": "J-001"}, {"$set": {"value": 100}})

if __name__ == "__main__":
    print("-----------------end-----------------")
