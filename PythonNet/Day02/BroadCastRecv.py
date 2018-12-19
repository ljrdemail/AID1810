# -*- coding:utf-8 -*-
# 广播示例：接收端

from socket import *

# 创建套接字

s = socket(AF_INET, SOCK_DGRAM)  # UDP套接字
# 设置可以接收广播
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
s.bind(("0.0.0.0", 9999))

while True:
    try:
        data, addr = s.recvfrom(1024)
        print("收到信息：", data.decode())
    except:
        print("接收异常")
        break

s.close()
