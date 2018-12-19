# -*- coding:utf-8 -*-
import pymysql
# 1 创建数据库连接对象
#db = pymysql.connect(host="176.136.16.13", user="tiger", pssword="123", database="db5", charset="utf8")
db = pymysql.connect("localhost", "root", "root", "db5", charset="utf8")
# 2 创建游标对象
cur = db.cursor()
# 3 利用游标对象的方法执行sql命令
s=cur.execute('insert into t1 values (5,"王昌龄",98)')
print(s)
# 4 提交到数据库
db.commit()
# 5 关闭游标
cur.close()
# 6 关闭数据库
db.close()
print("数据操作成功")
