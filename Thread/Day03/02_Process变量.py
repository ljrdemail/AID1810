import time
from multiprocessing import Process

# 定义 变量
name = "赵敏"


# 定义函数
def f1():
    global name
    print("子进程name=%s" % name)
    name = "周芷若"
    print("子进程修改了name=%s" % name)
    time.sleep(5)


# 创建进程对象
p = Process(target=f1)
p.start()
# time.sleep(0.1)
print("父进程name=%s" % name)
p.join()  # 处理僵尸进程 #阻塞函数 等待子进程结束之后 才执行父进程 p.join之后的语句 这里作用就是等子进程5秒 但是这样等于让父等待子 工作效率差
# 如果想要两个一起干活 把 print("父进程name=%s" % name)  放在start 和 join 之间
# p.join(3)  # 这样父进程只会等3秒 少于5秒 子进程变为孤儿进程

# 父进程
# print("父进程name=%s" % name)  # 深度拷贝 不会影响还是赵敏
# while True:
#     pass #产生僵尸进程
