# -*- coding:utf-8 -*-
from socket import *

client = socket(AF_INET, SOCK_DGRAM)
client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

addr = ("127.0.0.1", 9999)

client.sendto("你好服务器".encode(), addr)
data= client.recvfrom(1024)

print(data.decode())
client.close()
