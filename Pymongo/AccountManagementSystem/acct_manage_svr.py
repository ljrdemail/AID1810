# -*- coding:utf-8 -*-
from socket import socket

from pymongo import MongoClient

db_host = "127.0.0.1"
db_port = 27017
db_name = "test"
db_conn = None
address = ("0.0.0.0", 9999)


def conn_database():
    global db_conn
    db_conn = MongoClient(db_host, db_port)

    if not db_conn:
        print("连接数据库失败！")
        return -1
    else:
        return 1


def close_database():
    if not db_conn:
        return
    else:
        db_conn.close()


def query(msgs):  # 执行查询

    qry = None
    if msgs[1] == "all":
        qry = {}
    else:
        qry = {"acct_no": msgs[1]}
    print(qry)
    resp = ""  # 查询响应字符串
    try:
        dblist = db_conn.database_names()
        if db_name in dblist:
            mydb = db_conn[db_name]  # 相当于use test
            mycol = mydb["acct"]  # 获取集合对象
            docs = mycol.find(qry)  # 执行查询
            for doc in docs:
                acct_info = "账号:%s,户名:%s,余额:%s\n" % (doc["acct_no"], doc["acct_name"], doc["balance"])
                resp += acct_info


    except Exception as e:
        print(e)
        print("查询失败！")
    return resp


def new_account(msgs):
    ret = ""
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = float(msgs[4])

    mydict = {"acct_no": acct_no, "acct_name": acct_name, "acct_type": acct_type, "balance": balance}
    resp = ""
    try:
        dblist = db_conn.database_names()
        if db_name in dblist:
            mydb = db_conn[db_name]  # 相当于use test
            mycol = mydb["acct"]  # 获取集合对象
            ret = mycol.insert_one(mydict)
            if ret:
                resp = "插入成功，文档ID为：%s" % ret.inserted_id
    except Exception as e:
        print(e)
        resp = "插入记录失败！"

    return resp


def update_account(msgs):
    ret = ""
    acct_no = msgs[1]
    acct_name = msgs[2]
    acct_type = msgs[3]
    balance = float(msgs[4])

    mydict = {"acct_no": acct_no, "acct_name": acct_name, "acct_type": acct_type, "balance": balance}
    resp = ""
    try:
        dblist = db_conn.database_names()
        if db_name in dblist:
            mydb = db_conn[db_name]  # 相当于use test
            mycol = mydb["acct"]  # 获取集合对象
            query = {"acct_no": acct_no}
            new_value = {"$set": {"acct_name": acct_name, "acct_type": acct_type, "balance": balance}}
            ret = mycol.update_many(query, new_value) # 修改所有符合条件的记录
            if ret:
                resp = "共修改:%d行" % ret.modified_count
    except Exception as e:
        print(e)
        resp = "修改记录失败！"

    return resp


def delete_account(msgs):
    ret = ""
    acct_no = msgs[1]
    try:
        dblist = db_conn.database_names()
        if db_name in dblist:
            mydb = db_conn[db_name]  # 相当于use test
            mycol = mydb["acct"]  # 获取集合对象
            query = {"acct_no": acct_no}
            ret = mycol.delete_many(query) # 删除所有符合条件的记录
            resp = "删除了%d笔" % ret.deleted_count

    except Exception as e:
        print(e)
        resp = "删除记录失败！"

    return resp


def main():
    if conn_database() == -1:
        return  # 连接失败 返回
    server = socket()
    server.bind(address)
    server.listen()
    print("服务器启动成功！")
    sockfd, addr = server.accept()

    while True:
        data = sockfd.recv(2048)  # 接收数据
        if not data:
            print("客户端已经关闭")
            break
        # 解析，分发
        print(data.decode())
        msgs = data.decode().split("::")  #
        if (msgs[0] == "query"):
            result = query(msgs)
            if not result:
                result = "查无记录！"

        elif (msgs[0] == "new"):
            result = new_account(msgs)
        elif (msgs[0] == "update"):
            result = update_account(msgs)
        elif (msgs[0] == "delete"):
            result = delete_account(msgs)
        else:
            print("非法操作符！")
        sockfd.send(result.encode())
    close_database()
    server.close()


main()
