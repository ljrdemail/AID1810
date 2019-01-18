import string
import sys
from socket import *


def doRegist(client):

    while True:
        allChars = string.punctuation + string.whitespace
        username = input("\033[请输入注册的用户名：\033[0m")
        falg = 0
        for i in username:
            if (i in allChars):
                print("用户名中不能含有特殊字符!!!")
                flag = 1
                break;
        if flag:
            continue;


        # 输入密码
        # password1 = input("请输入密码！")
        # password2 = input("请再次输入密码")


def doLogin(client):
    pass


def doExit(client):
    pass


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
