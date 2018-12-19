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
    query = {}
    docs = mycol.find(query)  # 执行查询
    sortedDocs = docs.sort([("balance", pymongo.ASCENDING)])
    # sortedDocs = docs.sort([("balance", pymongo.DESCENDING)])
    for doc in docs:
        # print(doc)  # 这样也可以 就是格式有点乱
        acct_info = "账号:%s,户名:%s,余额:%s" % (doc["acct_no"], doc["acct_name"], doc["balance"])
        print(acct_info)
    # print(doc.acct_type) 因为上面制定了 所以在结果集里面没有所以不能打印

conn.close()
