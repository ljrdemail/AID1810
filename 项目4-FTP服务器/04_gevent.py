import time

import gevent


def f1(m, n):
    print("执行函数1", m, n)
    #time.sleep(2)#不是gevent类型阻塞 老老实实的等着
    gevent.sleep(2)
    print("函数1执行结束")


def f2():
    print('执行函数2')
    # time.sleep(3)
    gevent.sleep(3)
    print("函数2执行结束")


# 创建协程对象
g1 = gevent.spawn(f1, 10, 20)
g2 = gevent.spawn(f2)
# 启动所有协程 并在执行完毕之后回收协程 阻塞函数
gevent.joinall([g1, g2])
