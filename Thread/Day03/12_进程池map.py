import time
from multiprocessing import Pool


# 事件函数
def f1(n):
    #time.sleep(1)
    return n * n


# 创建进程池对象
pool = Pool(processes=6)

# 用map方式向进程池中添加任务
#返回值为事件函数的返回值列表
rlist = pool.map(f1, range(10000))
print(rlist)

# 关闭进程池
pool.close()

# 回收进程
pool.join()
