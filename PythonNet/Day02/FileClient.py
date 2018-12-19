# -*- coding:utf-8 -*-
# 简单客户端
from socket import *

addr = ("127.0.0.1", 9998)
client = socket()
client.connect(addr)

while True:
    filename = input("请输入你要上传的文件全路径！")
    try:
        fr = open(filename, 'rb')
        flag = 0

        while True:
            line = fr.read(4096)
            client.send(line)
            if not line:
                print("上传完成！")

                falg = 1
                break

        if flag == 1:
            break
    except:
     print("读写失败")

fr.close()
client.close()
print("客户端已关闭！")
