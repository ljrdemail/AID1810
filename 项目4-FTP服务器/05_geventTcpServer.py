import gevent
from gevent import monkey
# 必须放在socket之前导入 因为原理是第三方代码执行脚本 修改默认的阻塞行为
monkey.patch_socket()#如果不限定socket 可以patch_all()
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
        # 处理客户端请求函数
        # handle(client)
        # 协程，接收多个客户端的连接实现并发 比单线程高 但是不如多线程 多个协程在不同客户端切换 遇到阻塞就干别的线程
        gevent.spawn(handle, client)


def handle(client):
    while True:
        data = client.recv(1024)#在这里阻塞了 来回切换
        print("客户端说 %s" %(data.decode()))
        if not data:
            break
        client.send('服务端收到'.encode())

    client.close()


if __name__ == "__main__":
    Seerver()
