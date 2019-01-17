import os;


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
        os.exot("创建二级子进程失败")
    if (pid2 == 0):
        fun2()
    else:
        os.exit("关闭一级子进程")
else:
    pid, status = os.wait()
    fun1()
