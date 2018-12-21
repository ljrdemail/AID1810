import time
from multiprocessing import Pool


# 事件函数
def f1(n):
    # time.sleep(1)
    return n * n


if __name__ == "__main__":
    begin = time.time()
    pool = Pool(processes=6)
    rlist = []  # 用于存放函数的返回值
    for i in range(7):
        # 返回值为事件函数对象
        robj = pool.apply_async(func=f1, args=(i,))
        rlist.append(robj)
    # 遍历出rlist中的每一个元素（对象）,获取函数返回值
    #利用事件函数的get()方法获取返回值
    for r in rlist:
        print(r.get())
    pool.close()
    pool.join()
    end=time.time()
    print("程序执行时间:%.2f" %(end-begin))
