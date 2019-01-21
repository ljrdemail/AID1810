# 具体功能的实现
import sys
from socket import *


class FtpClient(object):
    pass


class Ftpclient(object):

    def __init__(self, client):
        # 把公用的client 通过构造函数拿进来
        self.client = client

    def doList(self):

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

    def doGet(self):
        pass

    def doPut(self):
        pass

    def doExit(self):
        self.client.send("Q".encode()
                         )
        sys.exit("感谢使用！")


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
        clientObj = Ftpclient(client)  # 多个客户端 不同的对象
        print("-------风云网盘-------")
        print("*** 1 查看文件列表 ***")
        print("*** 2 下载文件     ***")
        print("*** 3 上传文件     ***")
        print("*** 4 退出网盘     ***")
        print("-----------------------")
        cmd = input("\033[31m请选择(1/2/3):\033[0m")

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
