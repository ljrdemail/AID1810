# -*- coding:utf-8 -*-
from socket import *

sock_file = "sock_file"  # 程序运行目录创建文件

# 创建客户端
client = socket(AF_UNIX, SOCK_STREAM)
client.connect(sock_file)

while True:
    msg = input("请输入要发送的消息：")
    if not msg:
        continue
    if msg == "q" or msg == "Q":
        break;
    else:
        client.send(msg.encode())
client.close()
