# -*- coding:utf-8 -*-
import os

pid = os.fork()
if pid < 0:
    print("创建进程失败")
elif pid == 0:
    print("我是子进程，我的父进程是：%d:", os.getppid())
    print("我是子进程%d:",os.getpid())


else:
    print("我是父进程%d",os.getpid())

print("===========结束===================")
