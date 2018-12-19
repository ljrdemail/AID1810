# -*- coding:utf-8 -*-
import pymysql

db = pymysql.connect("localhost","root","root")
cursor = db.cursor()
cursor.execute("DROP DATABASE IF EXISTS indexdb;")
cursor.execute("create database indexdb character set utf8;")
cursor.execute("use indexdb;")
cursor.execute("create table t1(id int,name char(20));")
n = 1
name="lucy"
while n <= 2000000:
    cursor.execute("insert into t1 values('%s','%s')" % (n,name+str(n)))
    # n = int(n)
    n += 1
    print("第%d条数据插入成功" %n);
db.commit()
cursor.close()
db.close()