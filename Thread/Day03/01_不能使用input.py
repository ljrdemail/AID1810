import os
from multiprocessing import Process


def fun1():
    #multiprocessing 模块没有提供标准输入接口（不能用input）
    name = input("请输入姓名：") #报错 不支持基本输入


# 创建进程对象
p = Process(target=fun1)

# 创建进程并执行关联函数

p.start()

print("我是父进程！")


# pid = os.fork()
#
# if pid == 0:
#     name = input("请输入姓名：")
# else:
#     print("我是父进程！")
