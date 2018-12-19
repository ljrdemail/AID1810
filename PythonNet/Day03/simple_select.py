# 超时示例
# -*- coding:utf-8 -*-
from select import select
from socket import *

server = socket()
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 多个应用可以访问同同一个地址
server.bind(("0.0.0.0", 9999))
server.listen(10)
print("服务器已启动")

# 定义三个列表 存放 读 写 异常三类IO的列表
rlist = [server]  # 关注读事件的IO列表
wlist = []  # 关注写事件IO列表
xlist = []  # 关注异常事件IO列表

# 调用select,注册IO事件
while True:
    rs, ws, xs = select(rlist, wlist, xlist)  # 阻塞等待事件
    print("监控到有IO事件发生")
    # print(rs)
    # print(ws)
    # print(xs)
    # client, addr = server.accept()
    # print("Connect from:", addr)  # 打印客户端地址
    # 遍历返回IO列表，依次进行处理
    for r in rs:  # 读事件列表
        # 如果就绪的IO是监听socket
        # 如果就绪的IO是数据传输socket
        if r is server:
            client, addr = server.accept()  # 有多少个client连接过来 就有多少个client
            print("收到新的连接：", addr)
            rlist.append(client)  # 将客户端通信IO监控起来放入读事件列表
        else:
            data = r.recv(1024)
            if not data:  # ；连接有异常 比如对方关闭了 从关注事件里面去掉
                rlist.remove(r)
                continue
            else:
                print("收到数据:", data.decode())
                wlist.append(r) #加入写事件

    for w in ws:  # 写事件列表
       w.send(b"Test Msg") #b 代表后面字符传唤为字节
       # w.send("Test Msg".encode())
       wlist.remove(w) #如果不移除 就不停的发


    for x in xs:  # 异常事件列表
        pass

server.close()
