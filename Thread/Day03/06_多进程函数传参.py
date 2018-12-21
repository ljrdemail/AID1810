import os
import time
from multiprocessing import Process


# 事件1
def smoke(name, num):
    print("抽烟进程%d启动,%s吸了%d支烟" % (os.getpid(), name, num))


# 事件2

def drink(name):
    print("喝酒进程启动，%s正在喝酒" % name)


# 事件3

def hair(name):
    print("烫头进程启动,%s正在烫头" % name)


start = time.time()

# p1 = Process(target=smoke, args=("于谦", 5))
# p2 = Process(target=drink, args=("魏叔叔",))
# p3 = Process(target=hair, args=("超哥哥",))


p1 = Process(target=smoke, kwargs={"name": "于谦", "num": 5})
p2 = Process(target=drink, kwargs={"name": "魏叔叔"})
p3 = Process(target=hair, kwargs={"name": "超哥哥"})

p1.start()
p2.start()
p3.start()

p1.join()
p2.join()
p3.join()

end = time.time()

print("程序执行了：%.2f秒" % (end - start))
