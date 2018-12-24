from multiprocessing import Pipe
from multiprocessing import Process
#这个示例是延时 用父 conn1 发 子 conn2收

# 定义事件函数
def recive():
    # for i  in range(3):
    conn1.close()  # 子进程关闭发送端
    while True:
        try:
            data = conn2.recv()  # 一次只能收一条 如果父进程发了很多 过来也要用循环来收
            # 如果父进程只发了三条 range(4) 前面三条接收到之后 第四条 没收到就阻塞了
            # 解决方法通过套在while 发送端发送结束之后关掉连接 客户端catch EOFError 退出 While
            # 前提要求父进程关闭接收端 子进程关发送端
            # 因为只有关了 系统才知道 管道 不会再有信息流过了 因为 都只有一端 要么发送 要么接收
            # 才不会pend住 所以虽然管道既可以发送 也可接收 父子 肯定只有一方发送 一方接收 也就是砍掉每方的 一个端 才会抛出异常
            print("子进程接收数据:", data)
        except EOFError:

            break


# 父进程代码
# 创建管道(双向)

conn1, conn2 = Pipe()
# 创建进程对象
p = Process(target=recive)
p.start()
# 在发送之前关闭父进程的接收端
conn2.close()
# 父进程向管道发送数据
# conn2.send(123456)
for content in ["聂风", "步惊云", "孔慈"]:
    conn1.send(content)

# 关闭发送端：
conn1.close()

p.join()
