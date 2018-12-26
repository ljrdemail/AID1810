# 需求上半部分passwd1 下半部分passwd2
import os

fr = open("passwd", "r")  # 放在外面父子进程都可使用，假如说父进程先执行 把光标移动到了某个位置 CPU时间片到子进程 子进程字节把光标移动到了文件中间往后读


# 再切换到父进程的时候 父进程会继续沿着光标往后读
# 所以如果公用的是对象 指向同一片内存地址  就不能放在外面 都可以动就乱了 而且导致少拷贝数据


# 复制上半部分
def copy1():
    # fr = open("passwd", "r")
    fw = open("passwd1", "w")
    # 获取文件大小
    size = os.path.getsize("passwd")
    n = size // 2
    # 写入文件
    while True:
        if n < 1024:
            data = fr.read(n)
            fw.write(data)
            break
        data = fr.read(1024)
        fw.write(data)
        n = n - 1024
    fr.close()
    fw.close()


# 复制下半部分
def copy2():
    # fr = open("passwd", "r")
    fw = open("passwd2", "w")
    # 获取文件大小
    size = os.path.getsize("passwd")
    n = size // 2
    fr.seek(n, 0)  # 0表示从开始位置向后移动n个字节
    while True:
        data = fr.read(1024)
        if not data:
            break;
        fw.write(data)
    fr.close()
    fw.close()


if __name__ == "__main__":
    pid = os.fork()
    if pid < 0:
        print("创建线程失败！")
    elif pid == 0:
        copy2()
    else:
        copy1()
