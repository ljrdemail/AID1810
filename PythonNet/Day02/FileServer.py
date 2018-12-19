# -*- coding:utf-8 -*-
# 此示例延时简单网络服务器
from socket import *

server = socket()
address = ("0.0.0.0", 9998)
server.bind(address)
server.listen(10)
print("文件服务器已经启动")
filein, addr = server.accept()
filename = input("请输入目标文件名！")
try:
 fw = open(filename, 'wb')
 while True:

    data = filein.recv(4096)

    if  not  data  :

       break;
    else:
        fw.write(data)
 fw.close()
except :
    print("读写错误")


server.close()
