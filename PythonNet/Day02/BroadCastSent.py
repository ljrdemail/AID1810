# -*- coding:utf-8 -*-
# 广播示例程序：发送端
# 设置广播地址

# 176.136.16.41
# 255.255.255.0
# 176.136.16.255
from socket import *

dest = ("176.136.16.255", 9999)
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
msg = "这老师讲课让人打瞌睡"
s.sendto(msg.encode(), dest)
print("广播信息已发送")
s.close()
