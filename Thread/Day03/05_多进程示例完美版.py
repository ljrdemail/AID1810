import os
import time
from multiprocessing import Process


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


likes = [sing, dance, eat]
process = []

start = time.time()

for like in likes:
    # 创建进程对象
    p = Process(target=like)
    process.append(p)  # 添加进程对象到列表中等待后续用 join 回收
    # 启动进程
    p.start()
    # p.join() #不能这么写 否则启动进程 等进程处理完回收之后跳到下一个循环 创建另外一个进程 。。。。join阻塞
    #当唱歌进程还没结束 跳舞和吃货进程已经结束 此时操作系统会记录后面的完成状态 等sing结束后直接回收dance 和eat

for proc in process:
    # 回收进程
    proc.join() #逐个回收 不能第二个优先于第一个结束 先回收第二个 不行

end = time.time()

gap = end - start
print("运行时间经历了%.2f秒" % gap)
