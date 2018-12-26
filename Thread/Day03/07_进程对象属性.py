import os
import time
from multiprocessing import Process
from multiprocessing import current_process


# 写函数，每隔一秒打印当前时间，打印N次

def timming(n):
    for x in range(n):
        print(time.ctime())
        time.sleep(1)


# 创建进程
p = Process(target=timming, args=(7,), name="计时器")  # 只是创建了对象 只有等到start 才开始分配资源执行
print(p.name)  # 默认 process -1

# print(p.pid)
# print(p.is_alive())
# print(p.daemon)

# 启动进程
p.daemon = True  # 设置为守护进程 主进程结束 子进程跟着结束 要在start之前设定 要不然人家都启动了 玩毛
p.start()

# 进程创建起来之后才能有这些属性
print(p.pid)
print(p.is_alive())
print("通过current_process获取主进程pid:", current_process().pid)
print(os.getpid())
print(p.daemon)

# 回收进程
# p.join() # 和 p.daemon=True 矛盾 到底等不等？ 如果都写了，最后还是等（不会报错） 但是一般不会同时用 因为矛盾
