# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect("176.136.16.13", "tiger", "123", "db5", charset="utf8")

cur = conn.cursor()

ins = "insert into t1 values(6,'李清照',88)"
upd = "update t1 set name='蒲松龄' where id=1"
delt = "delete from t1 where id=2"

try:
    cur.execute(ins)
    cur.execute(upd)
    cur.execute(delt)
    conn.commit()
    print("数据库操作成功！")

except Exception as e:
    conn.rollback()
    print(e)
    print("数据库操作失败！")

cur.close()
conn.close()
