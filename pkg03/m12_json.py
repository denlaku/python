# coding=UTF-8
# pylint: disable=invalid-name
'''
json
'''
import json
arr = [{"name":'tom', "age": 100, "work": None}]

jsonstr = json.dumps(arr, indent=2, sort_keys=True)
print jsonstr
print type(jsonstr)

print json.loads(jsonstr)

if __name__ == "__main__":
    print "--------------------"
