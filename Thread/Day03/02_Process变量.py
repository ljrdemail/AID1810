import time
from multiprocessing import Process

# 定义 变量
name = "赵敏"


# 定义函数
def f1():
    print("子进程name=%s" % name)


# 创建进程对象
p = Process(target=f1)
p.start()
time.sleep(0.1)

# 父进程
print("父进程name=%s" % name)
