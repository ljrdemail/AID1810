# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect("176.136.16.14", "tiger", "123", "db5", charset="utf8")
cur = conn.cursor()

try:
    sel = "select * from t1"
    cur.execute(sel)
    line1 = cur.fetchone()
    print(line1)

    line2 = cur.fetchmany(2)  # 指针从第一条之后再取两条 不是从头开始取
    print(line2)  # 是个元组

    for m in line2:
        print(m) #打印每个元组
        print(m[1]) #打印元组中的某个值
        print(m[2])

    line3 = cur.fetchall()  # 指针从第3条之后再取两条 不是从头开始取
    print(cur.rowcount) #打印查询出来的条数
    print(line3)
    print(line3[0][1])
except:
    print("Failed")

cur.close()
conn.close()
