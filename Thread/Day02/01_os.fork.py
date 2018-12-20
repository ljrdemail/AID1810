# -*- coding:utf-8 -*-
import os
import time

pid = os.fork()  # 创建一个进程 只支持linux 操作系统 #在此复制一份代码
# 旧进程返回新复制进程的PID号 复制出来的进程pid此处返回0 所以新的 走了 我是新进程 老的 因为返回的pid是新进程的PID>0 所以走了 我是旧进程
# 复制的进程从os.fork() 之后执行 不是从头开始
# 被复制的是父进程 新的叫子进程
if pid < 0:
    print("创建进程失败")
elif pid == 0:
    time.sleep(0.1)
    print("我是新进程")
else:
    print("我是旧进程")

print("===========结束===================")
