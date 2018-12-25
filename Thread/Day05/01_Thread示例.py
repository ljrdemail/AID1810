import os
import time
from threading import Thread


# 线程函数
def music():
    for i in range(2):
        time.sleep(2)
        print("播放怒放的生命", os.getpid())#赋值线程进程号都是一个 因为共享线程资源


if __name__ == "__main__":
    # 创建线程对象
    t = Thread(target=music)
    # 启动线程

    t.start()
    # 主线程
    for i in range(2):
        time.sleep(3)
        print("播放学猫叫", os.getpid())#赋值线程进程号都是一个 因为共享线程资源



    t.join()
    # for i in range(2):
    #     time.sleep(3)
    #     print("播放学猫叫", os.getpid())  # 赋值线程进程号都是一个 因为共享线程资源
    # 如果主进程放在join下面 name 子进程打印完之后才到主进程