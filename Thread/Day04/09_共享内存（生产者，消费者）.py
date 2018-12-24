from multiprocessing import Lock
from multiprocessing import Process
from multiprocessing import Value


# 生产者
def makeMoney():
    for i in range(10000):
        # 加锁
        lock.acquire()
        money.value += 1
        lock.release()


# 消费者
def userMoney():
    for i in range(10000):
        lock.acquire()
        money.value -= 1
        lock.release()


if __name__ == "__main__":
    # 创建共享内存
    money = Value("i", 5000)

    # 创建锁对象
    lock = Lock()
    # 创建两个进程

    p1 = Process(target=makeMoney)
    p2 = Process(target=userMoney)
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("最终余额：", money.value)

# money.value = money.value + 1
# 内存中执行
# 第一步：先把money.value+1 赋值给temp 然后money.value=temp
# 第二步：money.value=x


# 正常执行过程 : money.value = 5000
# p1 : x1 = money.value + 1  ## x1->5001
# p1 : money.value = x1      ## money.value -> 5001
# p2 : x2 = money.value - 1  ## x2->5000
# p2 : money.value = x2      ## money.value -> 5000

# 异常执行过程 : money.value = 5000
# p1 : x1 = money.value + 1  ## x1 -> 5001
# p2 : x2 = money.value - 1  ## x2 -> 4999
# p2 : money.value = x2      ## money.value -> 4999 #时间片没有那么听话 等把x1 赋值给了money.value之后再切换到p2
# p1 : money.value = x1      ## money.value -> 5001


# 如何避免 对money.value加锁
