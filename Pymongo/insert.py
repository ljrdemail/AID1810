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

    # 插入的数据
    mydict = {"acct_no": "6225887842930823", "acct_name": "Timmy", "balance": 3333.33}
    ret = mycol.insert_one(mydict)  # 执行插入
    print("NewId:",ret.inserted_id) # 返回一个pymongo 对象 里面有很多属性


conn.close()
