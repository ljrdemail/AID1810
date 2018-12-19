# -*- coding:utf-8 -*-
# 此示例用于创建UDP连接的服务器端

from socket import *

address = ("0.0.0.0", 9999)
server = socket(AF_INET, SOCK_DGRAM)
server.bind(address)
print("服务器已经启动！")

while True:
    data, addr = server.recvfrom(1024)

    print("收到数据", data.decode())
    print("发送自：", addr)
    if not data:
        break
    resp = "你发送的信息已经收到：" + data.decode()

    server.sendto(resp.encode(), addr)

server.close()
