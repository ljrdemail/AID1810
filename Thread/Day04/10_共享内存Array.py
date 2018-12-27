from multiprocessing import Array
from multiprocessing import Process


# 事件函数

def f1():

    for i in shareData:
        print("子进程打印ShareData:", i)
    # x修改共享内存初始数据的第1 个元素
    #shareData[0] = 1000
    #shareData[0] = b'H'
    print("子进程修改第一个元素为：", shareData[0])




if __name__ == "__main__":
    # 开辟共享内存，存入整数列表
    #shareData = Array("i", [1, 2, 3, 4, 5])
    #shareData = Array("c", b'hello')
    shareData = Array("i", 6)
    p = Process(target=f1)

    for i in range(6):
        shareData[i]=i

    for i in shareData:
        print("父进程打印修改前的ShareData", i)
    p.start()
    p.join()
    for i in shareData:
        print("父进程打印修改后的ShareData", i)
