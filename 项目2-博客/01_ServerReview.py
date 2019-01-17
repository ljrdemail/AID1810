# -*- coding:utf-8 -*-
from socket import *

server = socket()
address = ("0.0.0.0", 9999)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(address)
server.listen(10)
print("等待客户端连接！")
socketfd, addr = server.accept();
data = socketfd.recv(1024);
print(data.decode())
socketfd.send("欢迎连接服务器！".encode())
socketfd.close()
server.close()
