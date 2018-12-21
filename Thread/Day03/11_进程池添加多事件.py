from  multiprocessing import Pool
import time

#事件1
def haiwang(n):
    print("海王在第%d次日海后湄拉" %n)
    time.sleep(1)


#事件2
def Trump(n):
    print("特例普在第%d次日梅拉尼亚" %n)
    time.sleep(1)

#创建进程池对象
p=Pool(processes=4)

#添加任务
for i in range(7):
    p.apply_async(func=haiwang,args=(i,))
    p.apply_async(func=Trump,args=(i,))
    time.sleep(1)

#关闭进程池
p.close()

#回收进程池
p.join()



