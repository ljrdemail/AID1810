import os
from socket import *


# 创建网络连接
def doLogin(server,user,name,addr):
    # 进入到聊天室请求处理函数
    if (name in user) or name=="管理员":
         server.sendto("该用户已经存在".encode(),addr)
         return
    #名字不存在发送OK给客户端
    server.sendto("OK".encode,addr)
    #通知其他人 这人已经登录
    message="欢迎"+name+"进入聊天室！"
    for u in user:
        server.sendTo(message.encode(),user[u])
        user[name]=addr






def doRequest(server):
    user = {}
    # 收消息
    while True:
        message, addr = server.recvfrom(1024)
        # [L,"金毛狮王"]
        meglist = message.decode().split(" ")
        print(meglist)
        if (meglist[0] == "L"):
            doLogin(server,user,meglist[1])


def main(clientHandler=None):
    server = socket(AF_INET, SOCK_DGRAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 9999))

    # 只进程负责管理员喊话，父进程负责和客户端交互

    pid = os.fork()
    if pid < 0:
        print('进程创建失败')
        return
    if pid == 0:
        # 子进程负责喊话
        print('负责管理员喊话的进程')

    else:
        # 父进程负责处理客户端的请求
        doRequest(server)


if __name__ == "__main__":
    main()
