from threading import Lock, Thread

m = 0
n = 0


# x线程函数
def f1():
    while True:
        ## 只要涉及到对临界资源操作的语句(临界区),需要加锁
        # 加锁
        lock.acquire()
        if m != n:
            print("m=", m, "n=", n)
        #释放锁
        lock.release()


if __name__ == "__main__":
    # 创建锁对象
    lock = Lock()
    t = Thread(target=f1)
    t.start()
    # 主线程要做的事情
    while True:
        with lock:#父进程加锁 确保正常+1
            m += 1
            n += 1
    t.join()
