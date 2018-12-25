import time
from threading import Thread


def f1(name, seconds):
    print("%s 线程开始执行" % name)
    time.sleep(seconds)
    print("%s线程执行完毕,时间%d 秒" % (name, seconds))


if __name__ == "__main__":

    # 创建空列表，用来存放线程对象
    threads = []
    for i in range(3):
        # t = Thread(target=f1, args=(i + 1, 2)) #元组传参
        #t = Thread(target=f1, kwargs={"name": "Tedu-%d" % i, "seconds": 2})#字典传参
        t=Thread(target=f1,args=("Tedu-%d" %i,),kwargs={"seconds":2})#混杂用 一般不这么玩
        threads.append(t)
        t.start()
    for i in threads:
        i.join()
