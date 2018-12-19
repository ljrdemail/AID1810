# -*- coding:utf-8 -*-
from socket import *

''' 数据格式
查询:
    请求:
        query::all    #查询所有账户信息
        query::622345000001 #查询指定账户
    响应:
        账号:622345000001, 户名:Jerry, 余额:10000

新增:
    请求:
        new::622345000002::Tom::1::10.00
    响应:
        执行1笔操作
 修改：
    请求：
     update::622345000002::Tom::1::10.00
     响应：
        执行1比操作
 删除：
    请求：
    delete：： 62234500002
    响应:
       执行1笔操作
'''

client = None
host = "127.0.0.1"
port = 9999


def print_menu():
    menu = '''
    ------账户管理系统-------
       1 - 查询账户
       2 - 新建账户
       3 - 修改账户
       4 - 删除账户
       5 - 退出  
    '''
    print(menu)


def open_connect():
    try:
        global client
        client = socket()
        client.connect((host, port))
        print("服务器连接成功！")
        return 0
    except:
        print("连接服务器失败！")
        return -1


def send_msg(msg):
    if not client:  # socket 没有被创建
        return -1
    n = client.send(msg.encode())  # 调用socket 发送
    return n


def recv_msg():  # 接收服务器响应
    if not client:
        return None
    data = client.recv(2048)  # 调用socket接收
    return data


def query_account():
    account_no = input("请输入要查询的账号：")
    if not account_no:  # 非空对象并且不是空串
        msg = "query::all"

    else:
        msg = "query::" + account_no
    if send_msg(msg) < 0:  # 调用函数发送请求
        print("发送失败！")
        return
    data = recv_msg()  # 接收查询结果
    if not data:
        print("查询失败")
    else:
        print(data.decode())  # 打印查询结果


def del_account():
    acct_no = input("请输入需要删除的账号：")
    msg = "delete::" + acct_no
    if send_msg(msg) < 0:  # 调用函数发送请求
        print("发送失败！")
        return
    data = recv_msg()  # 接收查询结果
    if not data:
        print("删除失败")
    else:
        print(data.decode())  # 打印查询结果


def new_acct():
    try:
        acct_no = input("请输入你要新增的账号：")
        acct_name = input("请输入你要新增的姓名：")
        acct_type = input("请输入修改后的账号类型（1-储蓄卡，2-信用卡）：")

        if (int(acct_type) !=1 and int(acct_type)!=2):
            print("输入错误必须为信用卡或储蓄卡！")
        balance = input("请输入你要新增的开户金额：")
        assert float(balance) >= 10.00

        msg = "new::" + acct_no + "::" + acct_name + "::" + str(acct_type) + "::" + balance
        if send_msg(msg) < 0:  # 调用函数发送请求
            print("发送失败！")
            return
        data = recv_msg()  # 接收查询结果
        if not data:
            print("插入失败")
        else:
            print(data.decode())  # 打印查询结果
    except AssertionError:
        print("金额不能小于10元")


def update_acct():
    try:
        acct_no = input("请输入你需要修改的账号：")
        acct_name = input("请输入修改后的新增的姓名：")
        acct_type = input("请输入修改后的账号类型（1-储蓄卡，2-信用卡）：")
        if (acct_type !=1 or acct_type !=2):
            print("输入错误必须为信用卡或储蓄卡！")

        balance = input("请输入修改后的账户余额：")
        assert float(balance) >= 10.00

        msg = "update::" + acct_no + "::" + acct_name + "::" + str(acct_type) + "::" + balance
        if send_msg(msg) < 0:  # 调用函数发送请求
            print("发送失败！")
            return
        data = recv_msg()  # 接收查询结果
        if not data:
            print("更新失败")
        else:
            print(data.decode())  # 打印查询结果
    except AssertionError:
        print("金额不能小于10元")


def main():  # 客户端的总入口
    open_connect()
    while True:
        print_menu()  # 打印菜单函数
        oper = input("请输入要执行的操作：")
        # if not oper:
        #     continue

        if oper == "1":
            query_account()
            continue

        if oper == "2":
            new_acct()
            continue
        if oper == "3":
            update_acct()
            continue
        if oper == "4":
            del_account()
            continue
        if oper == "5":
            print("感谢使用，欢迎下次再来！")
            break
        else:
            print("输入有误，请重新输入!")


main()
