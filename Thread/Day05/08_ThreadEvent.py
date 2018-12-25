from  threading import Thread,Event
import time

#定义一个全局变量
s=None

#分支线程事件函数

def python():
    global  s
    s="我待python如初恋"
    #把事件对象变为被设置
    e.set()#先设置为已设置
    #e.clear()#又变成未设置 主线程继续等着 当然 执行到e.set  cpu时间片就跑去主线程了 主线程就不用阻塞 但是几率太小

if __name__=="__main__":
    #创建事件对象
    e=Event()
    t=Thread(target=python)
    t.start()
    print("主线程：Python虐我千百遍")
    e.wait()#阻塞在此 初始e 为未设置状态 等待子进程修改时间对象变为已经设置，才往后执行下面的语句
    #e.wait(timeout=1)#理论上 两种可能都有 但是1 秒很长了 还是薪资过万
    if s=="我待python如初恋":
        print("恭喜，薪资过万！")
    else:
        print("下个班在等你！")