from multiprocessing import Process 
import time

# 定义变量 
name = "赵敏"
# 定义函数
def f1():
    # 声明全局变量
    global name
    print("子进程name=%s" % name)
    name = "周芷若"
    print("子进程修改了name=%s" % name)
    time.sleep(3)

# 创建进程对象
p = Process(target = f1)
p.start()

# 父进程和子进程同时做事,需要把父进程要做的代码放到
# start()和join()之间
# 父进程
print("父进程name=%s" % name)

# 回收子进程,阻塞函数
p.join()

