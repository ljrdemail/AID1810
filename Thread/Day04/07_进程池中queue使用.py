from multiprocessing import Pool, Manager


# 子进程1 负责放
def write():
    for s in ["A", "B", "C"]:
        q.put(s)


# 子进程2 负责取

def read():
    while True:
        try:
            print(q.get(block=False))  # 因为用了apply 等着放完 不会报错
            # print(q.get(block=True,timeout=1))
        except:
            break


if __name__ == "__main__":
    # 创建管道 进程池中创建管道必须用这个 不能直接queue
    q = Manager().Queue()
    pool = Pool()
    # 添加任务，用apply阻塞 先放再取
    pool.apply(func=write)
    #pool.apply_async(func=write) 如果非要async name 配合timeout
    pool.apply(func=read)
    #pool.apply_async(func=read)
    # 关闭进程池
    pool.close()
    pool.join()
