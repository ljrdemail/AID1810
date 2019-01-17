# -*- coding:utf-8 -*-
from socket import socket

client = socket()
address = ("127.0.0.1", 9999)
client.connect(address);

client.send("你好服务器！".encode())
data = client.recv(1024).decode()
print(data)

client.close()
