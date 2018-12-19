# -*- coding:utf-8 -*-
import pymongo

# 此示例用于连接mongo 并列出服务器中所有的库

# 建立到服务器的连接 MongoClinet
conn = pymongo.MongoClient("127.0.0.1", 27017)

# 列出所有的库

dblist = conn.database_names()
if not dblist:
    print("dblist is none")
else:
    for db in dblist:
        print("dbname：", db)
# 关闭数据库
conn.close()
