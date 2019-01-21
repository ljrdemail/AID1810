import os
import sys
import time
from socket import *

import pymysql


# 处理注册函数
def doRegist(client, db, username, password):
    # 判断user表中是否有此用户

    cursor = db.cursor()
    sel = 'select password from user where username=%s'
    # 根据要注册的用户名判断查询结果是否为空
    cursor.execute(sel, [username])
    # r结果为元组 用户不存在为空元组 否则为非空元组
    r = cursor.fetchall()
    if r:  # 如果不为空 代表用户已经存在
        client.send("EXITS".encode())
        return  # 回到调用他的函数  dorequest  然后回到while 循环打印一级界面
    else:
        # 不存在则插入
        sel2 = "insert into user(username,password) values (%s,%s)"
        try:
            cursor.execute(sel2, [username, password])
            db.commit()
            client.send("OK".encode())
        except Exception as e:
            db.rollback()
            client.send("FAIL".encode())


# 处理登录函数
def doLogin(client, db, username, password):
    sel = 'select password from user where username=%s'
    cursor = db.cursor()
    cursor.execute(sel, [username])
    r = cursor.fetchall()
    # 如果没有查到结果，表示用户名不存在
    if not r:
        client.send("NAMEERROR".encode())
    elif r[0][0] == password:
        # 密码正确 可以登录
        client.send("OK".encode())
    else:
        # 密码错误发送密码错误
        client.send("PWDERROR".encode())


# 把查询记录插入到history表函数
def doInsHistory(db, usename, word):
    cursor = db.cursor()
    ins = "insert into history(username,word,time) values(%s,%s,%s)"
    Time = time.ctime()
    try:
        cursor.execute(ins, [usename, word, Time])
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()


def doQuery(client, db, usename, word):
    # 我的版本
    # sel = "select interpret from words where word=%s"
    # sel2 = "insert into history(username,word,time) values(%s,%s,%s)"
    # cursor = db.cursor()
    # cursor.execute(sel, [word])
    # r = cursor.fetchall()
    #
    # cursor2 = db.cursor()
    # try:
    #     cursor2.execute(sel2, [usename, word, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())])
    #     db.commit()
    # except Exception as e:
    #     db.rollback()
    # if r:
    #     client.send(r[0][0].encode())
    #
    #
    # else:
    #     client.send("nodata".encode())

    # 老师的版本
    cursor = db.cursor()
    sel = "select interpret from words where word=%s"
    cursor.execute(sel, [word])
    # 获取查询结果
    result = cursor.fetchall()
    if not result:
        client.send("FAIL".encode())
        # 老师的版本如果查不到不记录到历史记录表
    else:
        # 单词解释
        client.send(result[0][0].encode())
        # 把查询记录插入到history表中
        doInsHistory(db, usename, word)


def doHistory(client, db, username):
    # 我的版本
    # sel = "select username,word,time from history where username=%s"
    # cursor = db.cursor()
    # cursor.execute(sel, [username])
    # r = cursor.fetchall()
    # message = ""
    # if not r:
    #     client.send("nodata".encode())
    # else:
    #     for m in r:
    #         message += m[0] + "," + m[1] + "," + m[2] + "$"
    #     client.send(message.encode())

    # 老师版本
    cursor = db.cursor()
    sel = "select * from history where username=%s"
    cursor.execute(sel, [username])
    result = cursor.fetchall()
    # esult:((1,hello,nihao),(),(),())
    if not result:
        client.send("FAIL".encode())
    else:
        client.send("OK".encode())
        time.sleep(0.1)  # 放置占包 避免OK 和后面的数据黏在一起 区分不开
        # 把result中的记录发给客户端
        for r in result:
            message = '%s %s %s' % (r[1], r[2], r[3])
            client.send(message.encode())
            time.sleep(0.1)  # 避免记录最后 和##分不开
            # 你的版本是通过整体发过去 在客户端解析所以不会有占包问题
        client.send("##".encode())


# 处理客户端请求函数
def doRequest(client, db):
    while True:
        message = client.recv(1024).decode()
        msgList = message.split(" ")
        # msgList: ['R','用户名','密码']
        if msgList[0] == "R":
            # 处理注册函数
            doRegist(client, db, msgList[1], msgList[2])
        elif msgList[0] == "L":
            # 处理登录函数
            doLogin(client, db, msgList[1], msgList[2])
            # 一级子界面退出功能
        elif msgList[0] == "E":
            sys.exit(0)
        elif msgList[0] == "Q":
            doQuery(client, db, msgList[1], msgList[2])
        elif msgList[0] == "H":
            doHistory(client, db, msgList[1])


# 搭建网络
def main():
    ADDRESS = ('0.0.0.0', 8888)
    # 创建数据库连接
    db = pymysql.connect('127.0.0.1', 'root', '123456', 'dict', charset='utf8')
    # 创建TCP套接字
    server = socket()
    # 设置端口复用
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(ADDRESS)
    server.listen(10)
    print("等待客户端连接")
    while True:
        try:
            client, addr = server.accept()
            print("客户端:", addr, "连接过来了")
        except KeyboardInterrupt:
            sys.exit("服务器宕机")
        except Exception  as e:
            print(e)
            continue  # 一般错误就继续干活
        # 创建进程 子进程和客户端交互 父进程等待其他客户端连接
        pid = os.fork()
        if pid < 0:
            print("创建进程失败！")
        elif pid == 0:
            # 子进程负责和客户端交互
            doRequest(client, db)
            sys.exit('客户端退出')
        else:
            # 父进程继续等待下一个客户端连接
            continue


if __name__ == "__main__":
    main()
