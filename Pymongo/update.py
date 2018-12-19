# -*- coding:utf-8 -*-
import pymongo

# 此示例用于连接mongo 并列出服务器中所有的库

# 建立到服务器的连接 MongoClinet
conn = pymongo.MongoClient("127.0.0.1", 27017)
# conn = pymongo.MongoClient("mongodb://localhost:27017")

dblist = conn.database_names()
dbname = "test"
if dbname in dblist:
    mydb = conn["test"]  # 相当于use test
    mycol = mydb["acct"]  # 获取集合对象
    query = {"acct_no": "6225887842930816"}

    new_value = {"$set": {"balance": 7777.66}}
    ret = mycol.update_one(query, new_value)  # 只会更新第一个找到的记录 想要更新多个 update_many

    print("共修改:%d行" % ret.modified_count)

conn.close()
