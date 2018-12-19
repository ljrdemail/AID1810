# 本地套接字的实例
# -*- coding:utf-8 -*-
import os
from socket import *

# 套接字文件
sock_file = "sock_file"  # 程序运行目录创建文件

if os.path.exists(sock_file):
    os.remove(sock_file)

# 创建套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)  # 要改为 AF_UNIX 不是AF_INET
sockfd.bind(sock_file)
sockfd.listen(3)

while True:
    client, addr = sockfd.accept()
    while True:
        data = client.recv(1024)
        print(data.decode())

sockfd.close()
