import os
import sys
from socket import *



# 子进程发消息函数
def sendMsg(client,name,addr):
    #子进程发消息给服务端 服务端 再进行转发 除他自己
    while True:
        content=input("请发言(quit退出):\n") #加一个空行避免 别的行打印到这一样
        if(content=="quit" or content=="exit"):
            message="Q "+name
            client.sendto(message.encode(),addr)
            sys.exit("退出聊天室")#子进程退出

        #包装消息
        message="C %s %s" %(name,content)
        client.sendto(message.encode(),addr)

# 父进程收消息函数
def recvMsg(client):
    while True:
        message,addr=client.recvfrom(1024)
        # 父进程退出
        if (message.decode() == "EXIT"):
            sys.exit("成功退出！")
        print(message.decode())


    # 创建套接字函数
def main():

    # 创建UDP套接字
    client = socket(AF_INET, SOCK_DGRAM)
    client.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    if len(sys.argv)<3:
        print('参数错误')
        return
    address=(sys.argv[1],int(sys.argv[2]))

    while True:
        name = input("请输入姓名：")
        message = "L " + name;
        # 向服务器发送消息
        client.sendto(message.encode(), address)
        # 接收服务器反馈
        data, addr = client.recvfrom(1024)
        if (data.decode() == "OK"):
            print("您已进入聊天室")
            #退出循环 不再输入用户名
            break
        else:
            print(data.decode())  # 打印从服务器发过来的不允许进入的原因

    # 创建进程 子进程发消息 父进程收消息
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败")
        # 子进程发消息
    elif pid == 0:
        sendMsg(client,name, addr)
    else:
        # 父进程收消息
        recvMsg(client)


if __name__ == "__main__":
    main()
