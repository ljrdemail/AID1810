from multiprocessing import Pipe
from multiprocessing import Process


# 定义事件函数
def recive():
    # for i  in range(3):
    conn2.close()   #单向管道也要关 因为单向只是没有send方法 还有别的方法 你要产生异常 文件描述符还是要关闭
    while True:
        try:
            data = conn1.recv()
            print("子进程接收数据:", data)
        except EOFError:

            break


# 父进程代码
# 创建管道(双向)

conn1, conn2 = Pipe(duplex=False) #只能conn2 发送 conn1 接收 否则报错 代表这个文件描述符没有发送或者接收的功能 其他功能还在
# 创建进程对象
p = Process(target=recive)
p.start()
# 在发送之前关闭父进程的接收端
conn1.close() #单向管道也要关 因为单向只是没有send方法 还有别的方法 你要产生异常 还是不许要关闭
# 父进程向管道发送数据
# conn2.send(123456)
for content in ["聂风", "步惊云", "孔慈"]:
    conn2.send(content)

# 关闭发送端：
conn2.close()

p.join()
