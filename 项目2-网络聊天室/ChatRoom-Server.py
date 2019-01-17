import os
from socket import *


# 创建网络连接
def doLogin(server, user, name, addr):
    # 进入到聊天室请求处理函数
    print(name in user)
    if (name in user) or name == "管理员":
        server.sendto("该用户已经存在".encode(), addr)
        return
    # 名字不存在发送OK给客户端
    server.sendto("OK".encode(), addr)
    # 通知其他人 这人已经登录
    message = '欢迎 %s 进入聊天室' % name
    for u in user:
        server.sendto(message.encode(), user[u])
    user[name] = addr
    print(user)


def doChat(server, content, user, name):
    msg = name + "说：" + content
    for u in user:
        if (u != name):
            server.sendto(msg.encode(), user[u])


def doQuit(server, name, user):
    # 通知其他成员
    message = name + "退出了聊天室！"
    for u in user:
        if (u != name):
            server.sendto(message.encode(), user[u])
        else:
            # 给退出者本人发消息
            server.sendto(b'EXIT', user[name])
    # 从存储结构中删除
    del user[name]


def doRequest(server):
    user = {}
    # 收消息
    while True:
        message, addr = server.recvfrom(1024)
        # [L,"金毛狮王"]
        meglist = message.decode().split(" ")  # 默认是空白作为分隔符
        print(meglist)
        if (meglist[0] == "L"):
            doLogin(server, user, meglist[1], addr)
        if (meglist[0] == "C"):
            content = ' '.join(meglist[2:])
            # 发给其他所有成员
            doChat(server, content, user, meglist[1])
        if (meglist[0] == "Q"):
            doQuit(server,meglist[1],user)


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
        # print('负责管理员喊话的进程')
        pass

    else:
        # 父进程负责处理客户端的请求
        doRequest(server)


if __name__ == "__main__":
    main()
