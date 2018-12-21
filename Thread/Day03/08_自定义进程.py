import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, n):
        # 使用super重新加载父类的__init__()方法
        # 如果不加载 会覆盖父类的
        super(MyProcess, self).__init__()
        self.n = n

    def fun1(self):
        for i in range(self.n):
            print("子进程在做事！")
            time.sleep(1)

    # 不用调用父类的run方法 因为要的就是覆盖

    # 重写run方法(名字不能变) 父类中对此方法做了自动化处理
    # 如果换了方法名 start就找不到了 所以不能改名
    def run(self):
        self.fun1()


if __name__ == "__main__":
    start = time.time()
    p = MyProcess(3)
    p.start()  # start 去调用run 方法
    p.join()
    end = time.time()
    print("我是父进程")
    print("执行时间:%.2f" % (end - start))
