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
    # query = {}  # 不带筛选条件
    # query={"acct_name":"Jerry"} #带一个条件
    # query = {"acct_name": "Jerry", "acct_no": "6225887842930816"} #带多个条件
    # query = {"balance": {"$gt": 5000}}
    query = {"$or": [{"acct_name": "Jerry"}, {"acct_name": "Emma"}]}  # 注意都要带上""
    # project = {"_id": 0}  # 不显示_id这个域 0 不显示 1 显示
    project = {"_id": False, "acct_no": True, "acct_name": True, "balance": True}
    docs = mycol.find(query, project)  # 执行查询
    for doc in docs:
        acct_info = "账号:%s,户名:%s,余额:%s" % (doc["acct_no"], doc["acct_name"], doc["balance"])
        print(acct_info)
    # print(doc.acct_type) 因为上面制定了 所以在结果集里面没有所以不能打印
    # print(doc) #这样也可以 就是格式有点乱

conn.close()
