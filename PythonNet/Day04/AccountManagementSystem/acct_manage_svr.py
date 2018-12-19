# -*- coding:utf-8 -*-

from socket import *

import pymysql

db_host = "127.0.0.1"
db_user = "root"
db_password = "root"
db_name = "accountmangsys"
db_conn = None
address = ("0.0.0.0", 9999)


def conn_database():
    global db_conn
    db_conn = pymysql.connect(db_host, db_user, db_password, db_name, charset="utf8")
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
    global db_conn
    cursor = db_conn.cursor()

    if msgs[1] == "all":
        sql = "select * from acct"
    else:
        sql = "select * from acct where acct_no=%s" % msgs[1]

    resp = ""  # 查询响应字符串
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            acct_no = row[0]
            acct_name = row[2]
            balance = row[4]
            acct_info = "账号：%s,户名：%s,余额：%.2f\n" % (acct_no, acct_name, balance)
            resp += acct_info
    except:
        print("查询失败！")
    return resp


def new_account(msgs):
    global db_conn
    cursor = db_conn.cursor()
    try:

        sql = "insert into acct (acct_no,acct_name,acct_type,balance,reg_date) values('%s','%s',%s,%s,now())" % (
            msgs[1], msgs[2], int(msgs[3]), float(msgs[4]))
        print(sql)
        res = cursor.execute(sql)
        cursor.execute("commit")
        if res:
            return "成功插入%d条记录！" % res
    except Exception as e:
        print(e)
        cursor.execute("rollback")
        return "插入记录失败！"


def update_account(msgs):
    global db_conn
    cursor = db_conn.cursor()
    try:

        sql = "update acct set acct_name='%s',acct_type=%s ,balance =%s ,reg_date=now() where acct_no ='%s'" % (
            msgs[2], int(msgs[3]), float(msgs[4]),msgs[1])
        print(sql)
        res = cursor.execute(sql)
        cursor.execute("commit")
        if res:
            return "成功修改%d条记录！" % res
    except Exception as e:
        print(e)
        cursor.execute("rollback")
        return "修改记录失败！"


def delete_account(msgs):
    global db_conn
    cursor = db_conn.cursor()
    try:

        sql = "delete from acct where acct_no='%s'" % (
            msgs[1])

        res = cursor.execute(sql)
        cursor.execute("commit")
        if res:
            return "成功删除%d条记录！" %res
    except Exception as e:
        print(e)
        cursor.execute("rollback")
        return "删除失败！"


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
