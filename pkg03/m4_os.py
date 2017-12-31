# coding=UTF-8
# pylint: disable=invalid-name
'''
os
'''
import os

# print dir(os)

# 修改文件名称, 如果文件不存在则报错
# os.rename("pkg02/c_os_001", "pkg02/c_os_002")
# 删除文件， 如果文件不存在则报错
# os.remove("pkg02/c_os_002")

# print os.listdir("pkg02")
# os.makedirs("pkg02/001")
# os.removedirs("pkg02/001")

# 获取文件的状态
# print os.stat("pkg02/b_sys.py")

print(os.getcwd())
os.chdir(os.pardir)
print(os.getcwd())
os.chdir("python-straining")
print(os.getcwd())

alls = os.listdir(os.curdir)
print(alls)
for f in alls:
    print(os.stat(f))



if __name__ == "__main__":
    print("--------------------")
