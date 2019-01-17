import os;
import sys
import time

pid = os.fork()
if pid < 0:
    print("创建线程失败")
    sys.exit("创建进程失败")
if pid == 0:
    print("新进程")
    time.sleep(1000)#避免僵尸进程

else:
    print("父进程")
