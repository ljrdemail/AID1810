import os;
import sys
from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind((("0.0.0.0"), 9999))
server.listen(10)
print("正在等待客户端连接")


def clientHandler(client, addr):
    # 二级子进程事件函数 负责和客户端交互
    print('客户端', addr, '连接接过来了')
    print(client)
    while True:
        data = client.recv(1024)
        if not data:
            break;
        print(addr, "说", data.decode())
        client.send('服务端收到'.encode())


while True:
    try:
        client, addr = server.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出");
    except Exception  as e:
        print(e)
        continue;
    # 创建子进程处理客户端请求
    pid = os.fork()
    if pid == 0:
        pid2 = os.fork()
        if pid2 == 0:
            # 创建二级子进程 与客户端交互
            # server.close()  # 不关闭也可以 关了是为了节省资源 client创建之后server  就没用了 可以关了
            clientHandler(client, addr)
            os._exit(0)  # 关掉二级子进程 是因为handler会是死循环 只要走到这一步代表client已经断开连接
        else:
            os._exit(0)  # 关掉一级子进程
    else:
        os.wait()  # 处理僵尸进程
        continue  # 继续等待其他客户连接
