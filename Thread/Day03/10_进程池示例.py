import time
from multiprocessing import Pool


# 定义事件函数
def automan(n):
    print("奥特曼进出进程池", n)
    time.sleep(1)


# 创建进程池对象
# pool = Pool(processes=2)
# pool = Pool(processes=6)
pool = Pool()  # 默认CPU核心数

# 添加任务
for i in range(1, 7):
    pool.apply_async(func=automan, args=(i,))
# pool.apply(func=automan, args=(i,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
