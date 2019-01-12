import pymysql

# 连接数据库
mysql = pymysql.connect(host="localhost", user="root", passwd="123456", db="py_mysql", charset="utf8")

# 获取操作游标
cur = mysql.cursor()
