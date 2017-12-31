# coding=UTF-8
# pylint: disable=invalid-name
'''
sys
'''
import requests

# get 请求
r = requests.get("https://hao.360.cn/")
print("----------cookies---------")
print(r.cookies)
print("----------headers---------")
print(r.headers)
print("----------content-type---------")
print(r.headers["content-type"])
print("----------status_code---------")
print(r.status_code)

print("----------text---------")
# print r.text


if __name__ == "__main__":
    print("--------------------")
