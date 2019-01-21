import getpass
import string
import sys
from hashlib import sha1
from socket import *


# 注册函数
def doRegist(client):
    while True:
        # 所有特殊字符 只要是用户名中含有这些特殊字符就不给注册
        allChars = string.punctuation + string.whitespace
        username = input("\033[31m请输入注册用户名:\033[0m")
        flag = 0
        for i in username:
            if (i in allChars):
                print("用户名中不能含有特殊字符!!!")
                flag = 1
                break;
        if flag:
            # 如果有特殊字符 回到循环继续重新输入
            continue;

        # 输入密码
        # getpass.getpass() 让输入的时候不显示明文
        password1 = getpass.getpass("请输入密码!")
        password2 = getpass.getpass("请再次输入密码!")
        # 判断两次密码是否一致
        if password1 == password2:
            # 创建sha1对象 并加密
            s = sha1()
            s.update(password1.encode())
            password = s.hexdigest()

        else:
            print("两次密码不一致")
            # 密码不一致 回到循环重新输入用户名和密码
            continue

        # 向服务端发送用户信息
        message = 'R %s %s' % (username, password)
        client.send(message.encode())
        # 等服务器反馈
        data = client.recv(1024).decode()
        if data == 'OK':
            print("注册成功!")
        elif data == "EXISTS":
            print("该用户已经存在！")
        else:
            print("注册失败！")
            # 服务器端     except Exception as e: 时候回报失败
        return  # 跳转一级界面 回到调用方


def doQuery(client, username):
    # 我的版本
    # while True:
    #     word = input("请输入你要查询的单词以##号结束：")
    #     if word == "##":
    #         break;
    #         return
    #     message = "Q %s %s" % (username, word)
    #
    #     client.send(message.encode())
    #     interpret = client.recv(1024).decode()
    #
    #     if interpret != "nodata":
    #         print("这个词的解释是:%s" % interpret)
    #     else:
    #         print("查无此单词")
    #         continue

    # 老师的版本
    while True:
        word = input("请输入你要查询的单词（##号退出）:")
        if word == "##":
            break
        # 包装消息
        message = "Q %s %s" % (username, word)
        client.send(message.encode())
        # 等到服务器返回
        data = client.recv(1024).decode()
        if data == "FAIL":
            print("词库中没有该单词！")
        else:
            print("单词解释：", data)  # 否则直接打印单词解释


def doHistory(client, username):
    # 我的版本
    # message = "H %s" % username
    # client.send(message.encode())
    # record = client.recv(1024).decode()
    #
    # if (record == "nodata"):
    #     print("无此人的历史记录数据")
    #     return
    # else:
    #     arr = record.split("$")
    #
    #     for i in range(0, len(arr) - 1):
    #         print("\t".join(arr[i].split(",")))
    # 老师版本
    # 包装消息 发送username 因为根据用户名查询记录
    message = "H %s" % username
    client.send(message.encode())
    # 等服务端反馈
    data = client.recv(1024).decode()
    if data == "OK":
        # 在服务端控制发送数量，此处循环接收
        while True:
            data = client.recv(1024).decode()
            if data == '##':
                break
            print(data)
    else:
        print("\033[32m没有历史记录！\033[0m")


# 二级子界面函
def doTwoLogin(client, username):
    while True:
        prompt = '''
               \033[32m===========二级子界面============
               --- 1.查词  2.历史记录  3.注销 ---
               ===============================
               请选择(1/2/3):\033[0m'''
        try:
            cmd = input(prompt)
            # 处理ctrl+c异常 退回到一级子界面
        except KeyboardInterrupt:
            break;
        if cmd not in ['1', '2', '3']:
            print("输入错误，必须为（1,2,3）")
            continue
        elif cmd == '1':
            doQuery(client, username)
        elif cmd == '2':
            doHistory(client, username)
        elif cmd == '3':
            # 终止此循环 回到一级子界面，嵌套循环
            break;  # 回到调用他的doLogin  然后跳到调用doLogin的main 回到while 打印一级子界面了


# 登录函数
def doLogin(client):
    username = input("请输入用户名:")
    password = getpass.getpass("请输入密码：")
    # 给密码加密(三步走)
    s = sha1()
    s.update(password.encode())
    password = s.hexdigest()
    # 包装消息并发送给服务端 注意空格不可少 因为用空格split
    message = 'L %s %s' % (username, password)
    client.send(message.encode())
    # 接收服务端反馈结果 注意decode
    data = client.recv(1024).decode()
    if data == 'OK':
        print('登录成功')
        # 进入二级子界面函数
        doTwoLogin(client, username)
    elif data == "NAMEERROR":
        # 用户名不存在
        print("用户不存在")
    else:
        # 用户名正确密码错误
        print("用户名或密码错误")


# 客户端退出函数
def doExit(client):
    client.send('E'.encode())
    sys.exit("客户端退出")


# 创建网络连接
def main():
    # 获取命令行参数
    if len(sys.argv) < 3:
        print('参数错误')
        return
    ADDRESS = (sys.argv[1], int(sys.argv[2]))
    # 创建UDP套接字
    client = socket()
    try:
        # 连接服务器
        client.connect(ADDRESS)
    except Exception as e:
        print(e)
        return

    # 客户端连接成功,进入一级界面
    while True:
        prompt = '''
        \033[31m**********一级界面***********
        --- 1.注册  2.登录  3.退出 ---
        ****************************
        请选择(1/2/3):\033[0m     
        '''
        try:
            cmd = input(prompt)
            # 处理异常 退出客户端
        except KeyboardInterrupt:
            doExit(client)
        if cmd.isdigit() and cmd in ['1', '2', '3']:
            if cmd == '1':
                # 注册函数
                doRegist(client)
            elif cmd == '2':
                # 登录函数
                doLogin(client)
            else:
                # 退出函数
                doExit(client)
        else:
            print("输入有误,请输入(1/2/3)!")


if __name__ == "__main__":
    main()
