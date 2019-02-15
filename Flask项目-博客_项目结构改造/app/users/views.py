# 处理与用户业务逻辑相关的视图和路由
from . import users
from .. import db
from ..models import *
from flask import render_template, request, session, redirect


@users.route("/login", methods=["GET", "POST"])
def login_view():
    if request.method == "GET":
        return render_template("login.html")
    else:
        # 接收前端传递过来的用户名和密码
        username = request.form.get("username")
        password = request.form.get("password")
        # 查询数据库 验证用户名和密码是否存在
        user = User.query.filter_by(loginname=username, upwd=password).first()
        # 根据结果保存进session
        if user:
            # 登录成功 保存数据进session 并且跳转到首页
            session["id"] = user.ID
            session["loginname"] = username
            return redirect("/")
        else:
            # 登录失败 返回到登录页面
            return redirect("/login")
