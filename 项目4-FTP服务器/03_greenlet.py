# 测试函数1
from greenlet import *


def f1():
    print(12)
    # 执行f1
    gr2.switch()
    print(34)
    gr2.switch()


# 测试函数2
def f2():
    print(56)
    gr1.switch()
    print(78)


# 创建协程对象
gr1 = greenlet(f1)
gr2 = greenlet(f2)

# 启动协程函数
gr1.switch()  # 12 56 34
