# -*- coding:utf-8 -*-
# 此示例用于说明socket 属性 方法测试示例

from socket import *

address = ("0.0.0.0", 9999)

s = socket()  # 不带参数就是流式socket

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# SO_REUSEADDR 设置端口可以服用
# 允许同一端口启动同一服务器的 多个示例

s.bind(address)

print("family:", s.family)  # 取地址类型
print("type:", s.type)  # 取套接字类型
print("getsockname:", s.getsockname())  # 地址
print("finano", s.fileno())#文件描述符
print("getsockopt:", s.getsockopt(SOL_SOCKET, SO_REUSEADDR)) # 获取setsockopt 中设定的 SO_REUSEADDR的值
