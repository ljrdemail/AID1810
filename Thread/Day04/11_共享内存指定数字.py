from multiprocessing import Process, Array


# 子进程把数据写入共享内存中
def f1(n):
    for i in range(n):
        arrayObj[i] = i+1



if __name__ == "__main__":
    # 创建共享内存，可存放3个整型数字
    arrayObj = Array("i", 3)
    p = Process(target=f1, args=(3,))
    p.start()
    p.join()
    #打印子进程存好的共享内存数据
    for i  in  arrayObj:
        print(i)

