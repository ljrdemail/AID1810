# 需求上半部分passwd1 下半部分passwd2
import os


# 复制上半部分
def copy1():
    fr = open("登录逻辑2.png", "rb")
    fw = open("登录逻辑21.png", "wb")
    # 获取文件大小
    size = os.path.getsize("登录逻辑2.png")
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
    fr = open("登录逻辑2.png", "rb")
    fw = open("登录逻辑22.png", "wb") #下半部分 打不开 因为上本部分才有标识这是个图片的数据 下半部分没有 所以打不开 但是数据是有的
    # 获取文件大小
    size = os.path.getsize("登录逻辑2.png")
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
