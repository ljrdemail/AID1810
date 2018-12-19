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

    List = [{"acct_no": "6225887842930824", "acct_name": "panpan", "balance": 3333.33},  # 库名称 字段名称 表名称都要用""括起来
            {"acct_no": "6225887842930825", "acct_name": "Peter", "balance": 6666.66},
            {"acct_no": "6225887842930826", "acct_name": "Candy", "balance": 9999.99}]  # 插入由字典组成的列表

    ret = mycol.insert_many(List)  # 执行插入
    print(ret.inserted_ids)  # 打印所有新产生的id

conn.close()
