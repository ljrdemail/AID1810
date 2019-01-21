import sys
#具体功能的实现
from socket import *

class FtpClient(object):
    pass

def main():
    if(len(sys.argv)<3):
        print("参数错误")
        return

    ADDRESS=(sys.argv[1],int(sys.argv[2]))
    #创建TCP套接字
    client=socket()
    try:
        client.connect(ADDRESS)
    except Exception as e:
        print('连接服务器失败',e)

        #连接成功，进入界面
        while True:
            print("------风云网盘------")
            print("***1 查看文件列表***")
            print("***  2 下载文件  ***")
            print("***  3 上传文件  ***")
            print("***  4 退出网盘  ***")
            print("---------------------")
            cmd=input("\033[31m请选择(1/2/3):\033[0m")

if __name__ == "__main__":
    main()