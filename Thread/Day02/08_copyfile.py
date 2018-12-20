# 需求上半部分passwd1 下半部分passwd2
import os


# 复制上半部分
def copy1():
    fr = open("passwd", "r")
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
    fr = open("passwd", "r")
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
