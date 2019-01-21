import sys
from socket import *
from threading import Thread

ADDRESS = ("0.0.0.0", 8888)
server = socket()
# 设定端口复用
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server.bind(ADDRESS)
server.listen(10)

# 等待接收客户端请求
print("服务器启动正常，等待客户端连接")


#处理客户端线程函数
def handler(client):
    while True:
        message=client.recv(1024)
        if not message:
            break;
        print(message.decode())
        client.send('服务端收到'.encode())

while True:
    try:
        client, addr = server.accept()
    except KeyboardInterrupt:
        sys.exot("服务器被强制退出")
    except Exception  as e:
        print(e)
        continue
    # 客户端连接过来了 创建线程 client 一定要传
    t = Thread(target=handler, args=(client,))
    t.setDaemon(True)  # 主线程挂了 子线程 一起挂  因为主线程就是服务器线程 服务器退出后 子线程（客户端） 也没有必要留着了 所以 可以设定为守护线程 避免阻塞问题
    t.start()
