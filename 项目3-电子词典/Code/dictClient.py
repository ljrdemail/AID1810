import getpass
import string
import sys
from hashlib import sha1
from socket import *


def doRegist(client):
    while True:
        allChars = string.punctuation + string.whitespace
        username = input("请输入注册的用户名:")
        flag = 0
        for i in username:
            if (i in allChars):
                print("用户名中不能含有特殊字符!!!")
                flag = 1
                break;
        if flag:
            continue;

        # 输入密码
        # getpass.getpass()
        password1 = getpass.getpass("请输入密码!")
        password2 = getpass.getpass("请再次输入密码!")
        # 判断两次密码是否一致
        if password1 == password2:
            # 创建sha1对象
            s = sha1()
            s.update(password1.encode())
            password = s.hexdigest()

        else:
            print("两次密码不一致")
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
        return  # 跳转一级界面 回到调用方


def doQuery(client, username):
    while True:
        word = input("请输入你要查询的单词以##号结束：")
        if word == "##":
            break;
            return
        message = "Q %s %s" % (username, word)

        client.send(message.encode())
        interpret = client.recv(1024).decode()

        if interpret != "nodata":
            print("这个词的解释是:%s" % interpret)
        else:
            print("查无此单词")
            continue


def doHistory(client, username):
    message = "H %s" % username
    client.send(message.encode())
    record = client.recv(1024).decode()

    if (record == "nodata"):
        print("无此人的历史记录数据")
        return
    else:
        arr = record.split("$")

        for i in range(0, len(arr) - 1):
            print("\t".join(arr[i].split(",")))


def doTwoLogin(client, username):
    while True:
        prompt = '''
        ==================二级子界面 ==================
        -------1 查询  2 历史记录  3 注销--------------
        =================================================
        请选择(1,2,3)
        '''
        cmd = input(prompt)
        if cmd not in ['1', '2', '3']:
            print("输入错误，必须为（1,2,3）")
            continue
        elif cmd == '1':
            doQuery(client, username)
        elif cmd == '2':
            doHistory(client, username)
        elif cmd == '3':
            # 终止此循环 回到一级子界面，嵌套循环
            break;  # 回到调用他的doLogin  然后跳到  调用他的 main 这个又是个死循环 就回到一级子界面了


def doLogin(client):
    username = input("请输入用户名:")
    password = getpass.getpass("请输入密码：")
    # 加密三部曲
    s = sha1()
    s.update(password.encode())
    password = s.hexdigest()
    # 包装消息
    message = 'L %s %s' % (username, password)
    client.send(message.encode())
    # 接收服务端反馈结果
    data = client.recv(1024).decode()
    if data == 'OK':
        print('登录成功')
        # 进入二级子界面函数
        doTwoLogin(client, username)
    elif data == "NAMEERROR":
        print("用户名错误")
    else:
        print("密码错误")


def doExit(client):
    client.send('E'.encode())
    sys.exit("客户端退出")


def main():
    if len(sys.argv) < 3:
        print('参数错误')
        return
    ADDRESS = (sys.argv[1], int(sys.argv[2]))

    # 创建UDP套接字
    client = socket()
    try:
        client.connect(ADDRESS)
    except KeyboardInterrupt:
        print("欢迎再次使用！")
    except Exception as e:
        print(e)
        return

    # 进入一级菜单
    while True:
        prompt = '''
        ***********一级界面***********
        --- 1.注册  2 登录   3 退出---
        *******************************
        请选择（1/2/3）      
        '''
        cmd = input(prompt)
        if cmd.isdigit() and cmd in ['1', '2', '3']:
            if cmd == '1':
                doRegist(client)
            elif cmd == '2':
                doLogin(client)
            else:
                doExit(client)
        else:
            print("输入有误，请重新输入（1,2,3）！")


if __name__ == "__main__":
    main()
