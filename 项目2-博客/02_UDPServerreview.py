# -*- coding:utf-8 -*-
from socket import *

server = socket(AF_INET, SOCK_DGRAM)

server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(("0.0.0.0", 9999))
while True:
    data, addr = server.recvfrom(1024)

    if not data:
        break;

    print(data.decode())

    server.sendto("客户端你好".encode(), addr)
server.close()
