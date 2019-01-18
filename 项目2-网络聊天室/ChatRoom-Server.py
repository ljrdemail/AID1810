import os
from socket import *


# 进入到聊天室请求处理函数
def doLogin(server, user, name, addr):
    if (name in user) or name == "管理员":  # 不能叫管理员
        server.sendto("该用户已经存在或使用了非法名字（管理员）".encode(), addr)
        return
    # 名字不存在，发送OK给客户端
    server.sendto("OK".encode(), addr)  # addr客户端的地址
    # 通知其他人 这人已经登录
    message = '\n欢迎 %s 进入聊天室' % name
    for u in user:
        server.sendto(message.encode(), user[u])
    # 加入存储结构user中
    user[name] = addr


# 聊天函数（把消息发给其他成员）
def doChat(server, content, user, name):
    # 包装消息

    msg ='\n%s说:%s' %(name,content)
    # 发给其他成员
    for u in user:
        if (u != name):  # 如果是管理员 这条永远成立 因为 列表中不可能有管理员 因为登录的时候要求neme!=管理员
            server.sendto(msg.encode(), user[u])


# 处理客户端退出函数
def doQuit(server, name, user):
    # 通知其他成员
    message = "\n"+name + "退出了聊天室！"
    for u in user:
        if (u != name):  # 排除退出者自己
            server.sendto(message.encode(), user[u])
        else:
            # 给退出者本人发消息 用于客户端收到信息之后干掉进程
            server.sendto(b'EXIT', user[name])
    # 从存储结构中删除
    del user[name]


def doRequest(server):
    user = {}
    # 收消息
    while True:
        message, addr = server.recvfrom(1024)
        # msgList: ['L', '金毛狮王']
        meglist = message.decode().split(" ")  # 默认是空白作为分隔符
        if (meglist[0] == "L"):
            doLogin(server, user, meglist[1], addr)
            # msgList: ['C','name','你好','步惊云']
        if (meglist[0] == "C"):
            content = ' '.join(meglist[2:])
            # 发给其他所有成员
            doChat(server, content, user, meglist[1])
        if (meglist[0] == "Q"):
            doQuit(server, meglist[1], user)


def main(clientHandler=None):
    # 创建网络连接
    # 创建UDP套接字
    server = socket(AF_INET, SOCK_DGRAM)
    # 设置端口复用
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # 绑定地址
    server.bind(("0.0.0.0", 9999))

    # 创建多进程，子进程负责管理员喊话，父进程和客户端交互

    pid = os.fork()
    if pid < 0:
        print('进程创建失败')
        return
    if pid == 0:
        # 子进程负责管理员发送消息
        # print('负责管理员喊话的进程')
        content = input("管理员消息:")
        # 对消息进行封装
        message = 'C 管理员 ' + content
        # 父进程在监听，把消息发送给父进程
        server.sendto(message.encode(), ("127.0.0.1", 9999))

    else:
        # 父进程负责处理客户端的请求
        doRequest(server)


if __name__ == "__main__":
    main()
