# -*- coding:utf-8 -*-
# 简单客户端
import socket

# 创建socket
address = ("127.0.0.1", 8888)  # 服务器的地址 端口
client = socket.socket()

##连接服务器
client.connect(address)
##发送数据 send()
while True:
    str = input("请输入你要发送的消息：")
    # msg = "This is test staring"
    client.send(str.encode())

    print("消息已经发送")
    data = client.recv(1024).decode()
    print(data)
    if (str == "exit"):
        break
    ##关闭连接
client.close()
print("客户端已关闭！")
