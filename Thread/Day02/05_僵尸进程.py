import os
import time

pid = os.fork()

if pid < 0:
    print("创建进程失败")

elif pid == 0:
    print("子进程:%d" % os.getpid())
    os._exit(0)


else:
    print("父进程:%d" % os.getpid())
    time.sleep(50)  # 让子进程先完成
