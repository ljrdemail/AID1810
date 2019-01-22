# 测试函数1
from greenlet import *


def f1():
    print(12)
    # 执行f1
    gr2.switch()#切到gs2  且一次如果没有继续切就盘完 gs2 如果切了就跑一句
    print(34)
    gr2.switch()#切到gs2


# 测试函数2
def f2():
    print(56)#切到gs1
    gr1.switch()
    print(78)#切到gs1


# 创建协程对象
gr1 = greenlet(f1)
gr2 = greenlet(f2)

# 启动协程函数
gr1.switch()  # 12 56 34
#greenlet 最大的特点是需要手工切换
