import time
from threading import Thread, Lock

# 创建2个锁对象
lock1 = Lock()
lock2 = Lock()

#假如说线程1  先执行
# 线程函数1
def f1():
    # lock1加锁
    lock1.acquire()  # 步骤1
    print("线程1 锁住了lock1")
    #遇到sleep()线程挂起 CPU 时间片到f2  请看f2
    time.sleep(0.1)
    # lock2加锁
    #给lock2加锁时候发现 f2 已经对lock2 进行了加锁 重复加锁导致阻塞
    lock2.acquire() # 步骤3 发现已经被f2 的步骤2 锁住
    print("线程1 锁住了lock2")
    print("线程1 你好")

    # 解锁
    lock2.release()
    lock1.release()


# 线程函数2
def f2():
    # lock1加锁
    lock2.acquire()#先锁住lock2  # 步骤2
    print("线程2 锁住了lock2")
    #此处遇到sleep() 线程2 挂起 CPU跑去f1
    time.sleep(0.1)
    # lock2加锁
    #f2 继续执行 发现 lock1 已经加锁了 阻塞

    lock1.acquire()  # 步骤4 发现已经被f1 步骤1 锁住
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
