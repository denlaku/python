# coding=UTF-8
# pylint: disable=invalid-name
'''
time
'''
import time

fmt = "%Y-%m-%d %H:%M:%S"
tstr = time.strftime(fmt, time.localtime(2000000000))
print(tstr)
print(time.strptime(tstr, fmt))

#获取格林威治时间
gt = time.gmtime()
print(gt)

# 获取本地时间
lt = time.localtime()
print(lt)
print(lt[0])

print(time.mktime(lt))
print(time.ctime())
print(time.asctime())

# 获取当前时间，从1970年1月1日0时0分0秒开始
print(time.time())


if __name__ == "__main__":
    print("--------------------")
