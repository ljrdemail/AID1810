import os;
import time


def fun2():
    print("子进程在执行")


def fun1():
    print("父进程在执行")

pid = os.fork();
if pid < 0:
    os.exit("创建进程失败")
if pid == 0:
    pid2 = os.fork()
    if (pid2 == 0):
        fun2()
    else:
        os._exit("关闭一级子进程")
else:
    pid, status = os.wait()
    fun1()
    time.sleep(30)