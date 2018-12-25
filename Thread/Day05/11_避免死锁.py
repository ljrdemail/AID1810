import time
from threading import Thread, Lock

# 创建2个锁对象
lock1 = Lock()
lock2 = Lock()

#假如说线程1  先执行
# 线程函数1
def f1():
    # lock1加锁
    lock1.acquire()
    print("线程1 锁住了lock1")
    #遇到sleep()线程挂起 CPU 时间片到f2  请看f2
    time.sleep(0.1)#sleep为了让时间片到另一个进程去
    # lock2加锁
    #给lock2加锁时候发现 f2 已经对lock2 进行了加锁
    while True: #放在while 下面 等f2 释放所有的锁
        result = lock2.acquire(timeout=1)
        if result:  # 如果result 为True 说明没死锁 继续走下面的程序  false就是死锁
            print("线程1 锁住了lock2")
            print("线程1 你好")

            # 解锁
            lock2.release()
            # lock1.release() 能走到这里 代表lock1 已经被f2释放了
            break

        else:
            lock1.release()  # 如果被f2 锁定了 lock2 那么解锁lock1 让f2 走下去 让它释放锁



# 线程函数2
def f2():
    # lock1加锁
    lock2.acquire()
    print("线程2 锁住了lock2")
    #此处遇到sleep() 线程2 挂起 CPU跑去f1
    time.sleep(0.1)#sleep为了让时间片到另一个进程去
    # lock2加锁
    #f2 继续执行 发现 lock1 已经加锁了 阻塞

    lock1.acquire()
    print("线程2 锁住了lock1")
    print("线程2 你好")

    # 解锁
    lock2.release()
    lock1.release()


t1 = Thread(target=f1)
t2 = Thread(target=f2)

t1.start()
t2.start()
t1.join()
t2.join()
