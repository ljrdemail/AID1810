import gevent
from gevent import monkey

# 必须放在socket之前导入 因为执行脚本 修改阻塞行为
monkey.patch_socket()
from socket import *


# 创建套接字
def Seerver():
    # 默认为TCP 套接字
    server = socket()
    ADDRESS = ('0.0.0.0', 8888)
    server.bind(ADDRESS)
    server.listen(10)
    print("正在等待客户端连接")
    while True:
        client, addr = server.accept()
        print(addr, "连接过来了")
        data = client.recv(1024).decode()
        print("客户端说:", data)
        # 处理客户端请求函数
        # handle(client)
        # 协程，接收多个客户端的连接实现并发
        gevent.spawn(handle, client)


def handle(client):
    while True:
        data = client.recv(1024)#在这里阻塞了 来回切换
        if not data:
            break
        client.send('服务端收到'.encode())
    client.close()


if __name__ == "__main__":
    Seerver()
