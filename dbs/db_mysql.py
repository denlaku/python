# coding=UTF-8
# pylint: disable=invalid-name
'''
mysql

1. MySQLdb (不推荐，2014年就已经不再维护了)
pip install mysql-python 命令安装无法成功
http://www.codegood.com/downloads
下载并安装MySQL-python-1.2.3.win-amd64-py2.7.exe

2. PyMySQL （推荐）
pip install  PyMySQL
'''

import pymysql
import pymysql.cursors

connection = pymysql.connect(host='localhost', user='den', password='denlaku',\
    port=3306, db='demo', charset='utf8')
cursor = connection.cursor()
sql = "select * from demo.t_user"
cursor.execute(sql)

result = cursor.fetchall()
# print result
print(cursor.description)
for row in result:
    # print row
    for f in row:
        print(f)

# conn = MySQLdb.connect(host="localhost", user="den", passwd="denlaku", db="demo", port=3306, characterEncoding="utf8")
# cur = conn.cursor()
# cur.exe("select * from demo.t_user")
# line = cur.findall()

if __name__ == "__main__":
    print("-----------------end-----------------")
