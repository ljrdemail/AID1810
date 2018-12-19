# 此示例演示通过网络传struct
# -*- coding:utf-8 -*-
import struct
from socket import *

address = ("127.0.0.1", 9999)

client = socket(AF_INET, SOCK_DGRAM)
while True:
    id = int(input("请输入id："))
    name = input("请输入姓名：")
    nlen = len(name)
    height = float(input("请输入身高："))
    struct.s
    fmt = "i%dsf"  %nlen
    data = struct.pack(fmt, id, name.encode(), height)
    client.sendto(fmt.encode(),address)
    client.sendto(data,address)
client.close()

