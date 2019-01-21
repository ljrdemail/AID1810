# 具体功能的实现
import sys
import time
from socket import *


class Ftpclient(object):

    def __init__(self, client):
        # 把公用的client 通过构造函数拿进来
        self.client = client

    def doList(self):
        # 向服务端发请求
        self.client.send(b"L")
        data = self.client.recv(1024).decode()

        # 接收
        if data == "OK":
            while True:
                filename = self.client.recv(1024).decode()
                if filename == "##":
                    break
                # 打印接收的文件名
                print("\033[31m" + filename + ":\033[0m")
        else:
            print(data)

    # 下载函数(收数据，写文件)
    def doGet(self):
        filename = input("请输入要下载的文件名：")
        message = "G %s" % filename
        self.client.send(message.encode())
        # 接收服务端反馈
        data = self.client.recv(1024).decode()
        if data == "OK":
            # 打开本地文件
            f = open(filename, 'wb')
            while True:
                data = self.client.recv(1024)
                if data == b"##":
                    break
                f.write(data)
            f.close()
            print("%s 下载完成" % filename)
        else:
            print(data)

    def doPut(self):
        filename = input("请输入要上传的文件：")
        # 用户输入可能为绝对路径或相对路径，按/进行切割
        # filename=filename.split("/")[-1] Linux
        filename2 = filename.split("\\")[-1]  # 为了不管输入全路径还是单独文件名都是截取文件名
        try:
            f = open(filename, 'rb')
        except:
            print("没这个文件")
            return
        message = "P " + filename2
        self.client.send(message.encode())
        data = self.client.recv(1024)  # 不用decode因为发过来的是文件内容的二进制
        if data == b'OK':
            # 读文件 发送数据
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.client.send(b'##')
                    break
                self.client.send(data)
            f.close()
            print("%s 上传完成" % filename2)
        else:
            print(data)

    def doExit(self):
        # 向服务端发送退出请求
        self.client.send("Q".encode())
        sys.exit("感谢使用！")


# 创建网络连接
def main():
    # if (len(sys.argv) < 3):
    #     print("参数错误")
    #     return

    ADDRESS = ("127.0.0.1", 8888)
    # ADDRESS = (sys.argv[1], int(sys.argv[2]))
    # 创建TCP套接字
    client = socket()
    try:
        client.connect(ADDRESS)
    except Exception as e:
        print('连接服务器失败', e)

        # 连接成功，进入界面
    while True:
        # 创建对象 调用类内的方法
        clientObj = Ftpclient(client)
        # 不同的客户端创建不同的对象
        print('\033[31m=========风云网盘==========\033[0m')
        print('***   1.查看文件列表     ***')
        print('***   2.下载文件        ***')
        print('***   3.上传文件        ***')
        print('***   4.退出网盘        ***')
        print('\033[31m==========================\033[0m')
        cmd = input('\033[31m请做出选择(1/2/3/4):\033[0m')

        # 做判断
        if cmd.strip() in ['1', '2', '3', '4']:
            if cmd == '1':
                clientObj.doList()
            if cmd == '2':
                clientObj.doGet()
            if cmd == '3':
                clientObj.doPut()
            if cmd == '4':
                clientObj.doExit()


        else:
            print("请输入(1/2/3/4)之间的数")


if __name__ == "__main__":
    main()
