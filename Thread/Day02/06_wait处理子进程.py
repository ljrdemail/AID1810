import os
import time
import sys

pid=os.fork()

if pid<0:
    print("进程创建失败！！")
elif pid==0:
    print("子进程于3 秒后退出！")
    time.sleep(3)
    sys.exit("子进程退出了") #status 当exit(0) status=0 当为非零 或字符串 status=256
else:
    pid,status=os.wait() #阻塞函数 当子进程退出后 解除阻塞
    print("pid:",pid)
    print("status:", status)
    print("子进程退出了，父进程已经处理完毕，没有僵尸进程 我可以继续执行了")
    while True: #死循环 确保子进程能处理完
        pass
