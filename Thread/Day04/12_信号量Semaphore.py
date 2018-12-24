import os
import time
from multiprocessing import Semaphore, Process


def f1():
    print("%d 想要执行事件" % os.getpid())
    sem.acquire()  # 拿到信号量的执行 信号量-1  只有3个拿到（因为信号量只有3） 其他7个没有拿到的阻塞 等着其中一个执行完+1 剩下7个进程抢
    # 直到其他7个都抢到 并执行完 程序结束
    print("%d 拿到信号量开始执行" % os.getpid())
    time.sleep(1)
    # 1个进程执行完成 信号量+1 变为1 这样剩余的7个进程 就有一个解除阻塞 执行任务
    sem.release()


if __name__ == "__main__":
    # 创建信号量
    sem = Semaphore(3)
    # 定义空列表，存放所有进程对象
    pList = []

    for i in range(10):
        p = Process(target=f1)
        pList.append(p)
        p.start()

    for p in pList:
        p.join()
