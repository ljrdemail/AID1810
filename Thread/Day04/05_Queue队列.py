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
    if not q.empty():
        while True:
            try:
                print(q.get(block=False))  # 不阻塞 没有值了就抛出异常 不用等别人再放了 因为是先放完 才开始取
                # 因为就那么多了 不会再放了 如果不这么写就卡死在这里等
            except Exception:
                print("队列已经空了")
                break


if __name__ == "__main__":
    # 创建队列
    q = Queue(4)
    p1 = Process(target=write)
    p2 = Process(target=read)
    # 让p1进程先执行 把所有的数据放队列中
    p1.start()
    p1.join()  # 先放好再取 join放这里
    p2.start()
    p2.join()
