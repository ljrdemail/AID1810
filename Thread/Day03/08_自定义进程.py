import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, n):
        # 使用super重新加载父类的__init__()方法
        # 如果不加载 会覆盖父类的
        super(MyProcess, self).__init__()
        self.n = n

    # 重写run方法
    def run(self):
        for i in range(self.n):
            print("子进程在做事！")
            time.sleep(1)


if __name__ == "__main__":
    start = time.time()
    p = MyProcess(3)
    p.start()
    p.join()
    end = time.time()
    print("我是父进程")
    print("执行时间:%.2f" % (end - start))
