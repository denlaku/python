# coding=UTF-8
# pylint: disable=invalid-name
'''
os
'''
import os
import yaml

# print dir(os)

# 修改文件名称, 如果文件不存在则报错
# os.rename("pkg02/c_os_001", "pkg02/c_os_002")
# 删除文件， 如果文件不存在则报错
# os.remove("pkg02/c_os_002")

# print os.listdir("pkg02")
# os.makedirs("pkg02/001")
# os.removedirs("pkg02/001")
print os.stat("pkg02/b_sys.py")


print "--------------------------------"
