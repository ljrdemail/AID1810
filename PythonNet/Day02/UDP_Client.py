# -*- coding:utf-8 -*-
# 此示例用于创建UDP连接的客户端

from socket import *

address = ("127.0.0.1", 9999)
client = socket(AF_INET, SOCK_DGRAM)

while True:
    data = input("请输入你要发送的信息：")
    if not data:
        continue
    if data == "Q" or data == "q":
        break;
    client.sendto(data.encode(), address)
    resp, addr = client.recvfrom(1024)

    if resp:
        print(resp.decode())

client.close()
