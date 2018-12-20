import os


# 事件1
def fun1():
    print("事件1")


# 事件2

def fun2():
    print("事件2")


pid = os.fork()

if pid < 0:
    print("一级子进程创建失败！")

elif pid == 0:
    p = os.fork()
    if p < 0:
        print("二级子进程创建失败！")

    elif p == 0:  # 二级子进程 要做的事情2
        fun2()
    else:  # 一级子进程要做的操作
        os._exit(0)  # 一级子进程结束
else:
    pid, status = os.wait()  # 阻塞，处理一级子进程
    fun1()  # 父进程做事件1
