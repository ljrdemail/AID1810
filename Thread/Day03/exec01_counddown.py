import time
from multiprocessing import Process


class MyCountDown(Process):
    def __init__(self, n):
        self.n = n
        super(MyCountDown, self).__init__()

    def fun1(self):
        print("倒计时%d秒开始" % self.n)
        for i in range(self.n, 0, -1):
            print(i)
            time.sleep(1)

    def over(self):
        print("比赛结束!!")

    def run(self):
        self.fun1()
        self.over()


if __name__ == "__main__":
    start = time.time()
    p = MyCountDown(10)
    p.start()
    p.join()
    end = time.time()
    print("程序执行了%.2f秒" % (end - start))
