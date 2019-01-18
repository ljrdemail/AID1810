import os
from socket import *
import sys

import pymysql


def doRequest(client):

    while True:
        message = client.recv(1024)
        print(message.decode())
        client.send("服务端收到".encode())


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
            doRequest(client)
            sys.exit('客户端退出')
        else:
            # 父进程继续等待下一个客户端连接
            continue

if __name__ == "__main__":
    main()
