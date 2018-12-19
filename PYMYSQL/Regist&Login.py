# -*- coding:utf-8 -*-
from _sha1 import sha1

from PYMYSQL.DbUtilP import DbUtil


def regist():
    du = DbUtil("176.136.16.13", "tiger", "123", "db5", "utf8", 3306)

    while True:
        username = input("请输入用户名：")
        lineone = du.DQL("select name from userInfo where name=%s", [username])

        if (len(lineone) != 0):
            print("用户已经存在！")
            continue;
        else:
            break

    while True:
        password = input("请输入密码：")
        password2 = input("请再次输入密码：")
        if (password != password2):
            print("两次输入密码不一致！")
            continue
        if (password == password2):
            break

    s = sha1()  # 创建加密对象
    s.update(password.encode("utf-8"))  # 参数是byte 所以encode
    pwd = s.hexdigest()  # 加密后转成16进制
    du.DML("insert into userInfo (name,password) values(%s,%s)", [username, pwd])


def login():
    username = input("请输入用户名：")

    du = DbUtil("176.136.16.13", "tiger", "123", "db5", "utf8", 3306)
    use = du.DQL("select name from userInfo where name=%s", [username])

    if (len(use) != 0):
        password = input("请输入密码：")
        pwddatabase = du.DQL("select password from userInfo where name=%s", [username])
        s = sha1()  # 创建加密对象
        s.update(password.encode("utf-8"))  # 参数是byte 所以encode
        pwd = s.hexdigest()  # 加密后转成16进制

        if (pwddatabase[0][0] == pwd):
            print("恭喜你，登录成功！")
        else:
            print("用户名或密码错误！")
    else:
        print("用户不存在！")


regist()
# login()
