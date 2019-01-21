import sys
from socket import *
from threading import Thread

# 定义全局变量
ADDRESS = ('0.0.0.0', 8888)


# 处理客户端线程函数
def doRequest(client):
    pass


# 具体功能实现类
class FtpServer(object):
    pass


# 创建网络连接
def main():
    server = socket()
    # 设定端口复用
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(ADDRESS)
    server.listen(10)

    # 等待接收客户端请求
    print("服务器启动正常，等待客户端连接")

    while True:
        try:
            client, addr = server.accept()
        except KeyboardInterrupt:
            sys.exit("服务器被强制退出")
        except Exception  as e:
            print(e)
            continue
        t = Thread(target=doRequest(), args=(client,))
        t.setDaemon(True)  # 主线程挂了 子线程 一起挂  因为主线程就是服务器线程 服务器退出后 子线程（客户端） 也没有必要留着了 所以 可以设定为守护线程 避免阻塞问题
        t.start()


if __name__ == "__main__":
    main()
