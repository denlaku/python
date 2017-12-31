# coding=UTF-8
# pylint: disable=invalid-name
'''
url lib
'''
import urllib
from urllib import parse
from urllib import request
params = {
    "name": "AA",
    "code": "E001"
}

print(urllib.parse.__all__)
print(urllib.request.__all__)
print(urllib.response.__all__)
print(urllib.error.__all__)

# print(urllib.urlencode(params))
print(parse.urlencode(params))
# #对URL进行编码
print(parse.quote("中国"))
# #对字符串进行解码
print(parse.unquote("%E4%B8%AD%E5%9B%BD"))

# urllib.urlretrieve("http://localhost:8080/boot/api/user/findById/41", "user.json")
uparse = parse.urlparse("http://localhost:8080/boot/api/user/findById/41?name=AA&code=E001")
print(uparse)
print(parse.urlunparse(uparse))

# urllib.urlretrieve('https://p1.ssl.qhimg.com/t0151320b1d0fc50be8.png', "t_001.png")

# baidu = urllib.urlopen("https://www.baidu.com/")
baidu = request.urlopen("https://www.baidu.com/")

print(baidu.geturl())
# 获取头信息
print(baidu.getcode())
# print baidu.info()
# print baidu.read()


if __name__ == "__main__":
    print("--------------------")
