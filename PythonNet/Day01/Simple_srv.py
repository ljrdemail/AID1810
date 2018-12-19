# -*- coding:utf-8 -*-
# 此示例延时简单网络服务器
import socket

# 创建socket
server = socket.socket()
address = ("0.0.0.0", 9999)  # 监听本机所有的IP地址 所有IP 这个端口都监听 一台机器可以有多个IP地址
##绑定地址:bind()函数
server.bind(address)
##监听 listen() 函数
server.listen(10)  # 允许有多少个连接在哪里等
print("服务器已启动：", address)
# 接收请求accept()
sockfd, addr = server.accept()
while True:
    print("收到客户端请求", addr)
    ##数据接收recv()
    data = sockfd.recv(1024)  # 不能超过1024 否则截取 从缓冲区里面接受1024个自己 如果缓冲区没有等待
    if not data:
        break
    print(data.decode())

##关闭连接
# sockfd.close()
server.close()
