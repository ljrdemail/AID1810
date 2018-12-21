import os
from multiprocessing import Process
import time


# 事件1
def sing():
    print("唱歌进程启动，我的父进程是:%d" % os.getppid())
    time.sleep(1)


# 事件2

def dance():
    print("跳舞进程启动，我的父进程是:%d" % os.getppid())
    time.sleep(1)


# 事件3

def eat():
    print("吃货进程启动，我的父进程是:%d" % os.getppid())
    time.sleep(1)


start=time.time()
# 创建进程对象
p1 = Process(target=sing)
p2 = Process(target=dance)
p3 = Process(target=eat)

# 启动进程
p1.start()
p2.start()
p3.start()

# 回收进程
p1.join()
p2.join()
p3.join()
end=time.time()

gap=end-start
print("运行时间经历了%.2f秒" %gap)