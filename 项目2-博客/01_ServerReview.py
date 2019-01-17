# -*- coding:utf-8 -*-
from socket import socket

server = socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind("0.0.0.0", 8888)
server.listen(10)
socketfd, addr = server.accept();
data = socketfd.recv(1024);
print(data.decode())
socketfd.send("欢迎连接服务器".encode())
socketfd.close()
server.close()
