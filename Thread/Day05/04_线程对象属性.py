import time
from threading import Thread,current_thread




# 事件函数
def f1():
    print("线程对象t属性测试")

    time.sleep(1)
    print("子线程执行完毕%s" %current_thread().getName())#通过这种方式能在子进程中打印当前线程的线程名 默认Thread-1


if __name__ == "__main__":
    t = Thread(target=f1)
    # 设置守护线程，一定要写在start()之前 不能和 join同时用 不会报错但是没有意义
    # t.daemon = True  # 默认False
    # t.setDaemon(True)  # 两种方式都可以
    t.start()
    # 线程中可利用name属性或者getName()方法获取线程名
    print("线程名称：", t.name)  # 放在start 后面 默认 Thread-1
    print("线程名称：", t.getName())  # 跟上面等效 这个方法线程独有
    t.setName("Tedu-1")  # 这个方法线程独有
    print("线程名称：", t.name)  # 放在start 后面
    print("主进程结束")
    t.join() #setSaemon要注释掉这个
