import time
from multiprocessing import Process
from threading import Thread


# CPU密集型
def CPU(x, y):
    z = 0
    while z < 7000000:
        x += 1
        y += 1
        z += 1


# 本地磁盘IO密集型
def write():
    f = open("text.txt", "a")
    for i in range(150000):
        f.write("hello world \n")
    f.close()


def read():
    f = open("text.txt")
    lines = f.readlines()
    f.close()


def IO():
    write()
    read()


# 多线程处理CPU密集型
begin = time.time()
threads = []
for i in range(10):
    t = Thread(target=CPU, args=(1, 1))
    threads.append(t)
    t.start()

for m in threads:
    m.join()
end = time.time()
print("多线程处理CPU密集型：%.2f" % (end - begin))

# 多进程处理CPU密集型

begin = time.time()
process = []
for i in range(10):
    p = Process(target=CPU, args=(1, 1))
    process.append(p)
    p.start()

for m in process:
    m.join()
end = time.time()
print("多进程处理CPU密集型：%.2f" % (end - begin))

#多线程执行IO密集
begin = time.time()
threads = []
for i in range(10):
    t = Thread(target=IO)
    threads.append(t)
    t.start()

for m in threads:
    m.join()
end = time.time()
print("多线程处理IO密集型：%.2f" % (end - begin))

#多进程执行IO密集

begin = time.time()
process = []
for i in range(10):
    p = Process(target=IO)
    process.append(p)
    p.start()

for m in process:
    m.join()
end = time.time()
print("多进程处理IO密集型：%.2f" % (end - begin))