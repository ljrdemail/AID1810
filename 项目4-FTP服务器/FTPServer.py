import os
import sys
import time
from socket import *
from threading import Thread

# 定义全局变量
ADDRESS = ('0.0.0.0', 8888)

filDir = "D:\\AID1810\\项目4-FTP服务器\\ftpFile\\"


# filDir="/home/tarena/AID1810/项目4-FTP/ftpFile"


# 处理客户端线程函数
def doRequest(client):
    # 接收客户端的各种请求
    while True:
        serverObj = FtpServer(client)
        # 接收客户端发过来的包装好的请求
        message = client.recv(1024).decode()
        msgList = message.split(' ')
        if msgList[0] == 'L':
            serverObj.doList()
        elif msgList[0] == 'G':
            serverObj.doGet(msgList[-1])  # 用-1 是为了避免用户输入了空格之后 再输入文件名
        elif msgList[0] == 'P':
            serverObj.doPut()
        elif msgList[0] == 'Q':
            serverObj.doExit()


# 具体功能实现类
class FtpServer(object):
    def __init__(self, client):
        self.client = client

    def doList(self):

        # 利用OS模块把内容放到列表当中
        fileList = os.listdir(filDir)

        if not fileList:
            self.client.send('文件库为空'.encode())
        else:
            self.client.send(b'OK')
            time.sleep(0.1)  # 防止粘包 OK 和内容
            # 发送文件名到客户端
            for file in fileList:
                # 判断是否为普通文件 排除文件夹和隐藏文件
                if os.path.isfile(filDir + file) and file[0] != '.':
                    self.client.send(file.encode())
                    time.sleep(0.1)  # 防止粘包 内容和##
            self.client.send("##".encode())

    def doGet(self, filename):
        try:
            f = open(filDir+filename, 'rb')
        except:
            self.client.send('文件不存在'.encode())
            return

        # 文件夹正常打开
        self.client.send("OK".encode())
        time.sleep(0.1)  # 防止粘包
        while True:
            data = f.read(1024)
            if not data:
                time.sleep(0.1) #15:56
                self.client.send("##".encode())
                break
            else:
                self.client.send(data)
        f.close()

    def doPut(self):
        pass

    def doExit(self):
        sys.exit(0)


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
        t = Thread(target=doRequest(client), args=(client,))
        t.setDaemon(True)  # 主线程挂了 子线程 一起挂  因为主线程就是服务器线程 服务器退出后 子线程（客户端） 也没有必要留着了 所以 可以设定为守护线程 避免阻塞问题
        t.start()


if __name__ == "__main__":
    main()
