# 超时示例
# -*- coding:utf-8 -*-
from socket import *

address = ("127.0.0.1", 9999)
client = socket()
client.settimeout(5)
client.connect(address)
print("连接服务器成功")
client.send("test msg".encode())
print("发送成功")
client.recv(1024)  # 接收超时
client.close()
