import time

import gevent


def f1(m, n):
    print("执行函数1", m, n)
    #time.sleep(2)#不是gevent类型阻塞 老老实实的等着 一共5秒
    gevent.sleep(2) #一共3秒
    print("函数1执行结束")


def f2():
    print('执行函数2')
    # time.sleep(3)#不是gevent类型阻塞 老老实实的等着 一共5秒
    gevent.sleep(3) #一共3秒
    print("函数2执行结束")


# 创建协程对象
g1 = gevent.spawn(f1, 10, 20)
g2 = gevent.spawn(f2)
# 启动所有协程 并在执行完毕之后回收协程 阻塞函数 把需要管理的协程放入列表 然后交给joinall就好
gevent.joinall([g1, g2])
