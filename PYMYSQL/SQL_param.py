# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect("176.136.16.13", "tiger", "123", "db5", charset="utf8")
cur = conn.cursor()

sid = input("请输入id号：")
sname = input("请输入诗人的姓名：")
sscore = input("请输入诗人的分数：")

#ins = "insert into t1 values (%s,%s,%s)"
ins = "insert into t1 values ('%s','%s','%s')" %(sid,sname,sscore) #这种方式不推荐 而且万一字段中由" ' 就会报SQL错误 因为视为结束标志
#L = [sid, sname, sscore]

try:
    #cur.execute(ins, L)
    cur.execute(ins)
    conn.commit()
    print("OK")
except Exception as e:
    conn.rollback()
    print("Failed", e)

cur.close()
conn.close()
