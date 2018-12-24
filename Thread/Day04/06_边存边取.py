from multiprocessing import Queue, Process


# 子进程1 在队列中添加消息
def write():
    for i in range(10):
        if q.full():
            print("队列满")
            break
        q.put(i)


# 子进程2在队列中获取消息
def read():
    # 当队列不为空时获取数据

        while True:
            try:
                print(q.get(block=True,timeout=1))# 去掉not empty 因为刚开始有可能队里是空的 等着写放 如果1秒还一个都没有放 则报错
            except Exception:
                print("队列已经空了")
                break


if __name__ == "__main__":
    # 创建队列
    q = Queue(4)
    p1 = Process(target=write)
    p2 = Process(target=read)

    p1.start() #两个进程同时启动  不用等写完
    p2.start()
    p1.join()
    p2.join()
