import os
import sys
from socket import *

import pymysql


def doRegist(client, db, username, password):
    # 判断user表中是否有此用户
    print(password)
    cursor = db.cursor()
    sel = 'select password from user where username=%s'
    cursor.execute(sel, [username])
    # r结果为元组 用户不存在为空元组 否则为非空元组
    r = cursor.fetchall()
    if r:
        client.send("EXITS".encode())
        return
    else:
        sel2 = "insert into user(username,password) values (%s,%s)"
        try:
            cursor.execute(sel2, [username, password])
            db.commit()
            client.send("OK".encode())
        except Exception as e:
            db.rollback()
            client.send("FAIL".encode())


def doRequest(client, db):
    while True:
        message = client.recv(1024).decode()
        msgList = message.split(" ")
        if msgList[0] == "R":
            # 处理注册函数
            doRegist(client,db, msgList[1], msgList[2])


def main():
    ADDRESS = ('0.0.0.0', 8888)
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
            continue
        # 创建进程 子进程和客户端交互 父进程等待其他客户端连接
        pid = os.fork()
        if pid < 0:
            print("创建进程失败")
        elif pid == 0:
            # 子进程负责和客户端交互
            doRequest(client, db)
            sys.exit('客户端退出')
        else:
            # 父进程继续等待下一个客户端连接
            continue


if __name__ == "__main__":
    main()
