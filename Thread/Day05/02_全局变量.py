import os
import time
from threading import Thread

n = 1


# 线程函数
def music():
    for i in range(2):
        time.sleep(2)
        print("播放怒放的生命", os.getpid())  # 父子进程号都是一个 因为共享线程资源
    # 在子线程中更改变量
    global n
    n = 1000
    print("分支线程:n=", n)


if __name__ == "__main__":
    # 创建线程对象
    t = Thread(target=music)
    # 启动线程

    t.start()
    # 主线程
    # for i in range(2):
    #     time.sleep(3)
    #     print("播放学猫叫", os.getpid())#父子进程号都是一个 因为共享线程资源

    t.join()

    for i in range(2):
        time.sleep(3)
        print("播放学猫叫", os.getpid())  #父子进程号都是一个 因为共享线程资源
    print("主线程中n的值：", n) #线程共享进程的资源 一个线程 修改了 别的线程会受到影响 类似于共享内存
    # 如果主进程放在join下面 name 子进程打印完之后才到主进程
