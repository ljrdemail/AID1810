from multiprocessing import Pool, Manager


# 子进程1 放

def f1(n):
    for i in range(1, n + 1):
        # 放元组
        q.put((2, i))


# 子进程取
def f2(n):
    for i in range(1, n + 1):
        pass
        # 因为已经直到多少次了就不用except catch
        m, n = q.get()
        # 2的n次方
        print(m ** n)


if __name__ == "__main__":
    # 创建消息队列（进程池）
    q = Manager().Queue()
    pool = Pool()
    pool.apply(func=f1, args=(10,))
    pool.apply(func=f2, args=(10,))
    pool.close()
    pool.join()
