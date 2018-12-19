# 超时示例
# -*- coding:utf-8 -*-
import time
from socket import *

address = ("0.0.0.0", 9999)
s = socket()
s.bind(address)
s.listen(10)

print("服务器启动:", address)

sockfd, addr = s.accept()
print("收到客户端请求:", addr)
data = socket.recv(1024)  # 接收
print(data)
time.sleep(10)
time.sleep(10)
sockfd.send("time out test msg".encode())
sockfd.close()
s.close()
