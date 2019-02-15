# 处理与博客相关的路由和视图
from . import main
from flask import render_template, session, request
from ..models import *
from .. import db


@main.route('/')
def main_index():
    # 查询Category中所有的分类信息
    categories = Category.query.all()
    topics = Topic.query.all()
    # 判断session中是否有id 和loginname的值
    if "id" in session and "loginname" in session:
        # 已经登录过 从数据库中获取登录信息
        id = session["id"]
        user = User.query.filter_by(ID=id).first()

    return render_template('index.html', params=locals())


@main.route("/release", methods=["GET", "POST"])
def release_views():
    if request.method == "GET":
        # 权限验证 判断是否有用户登录一级登录者的身份是否为作者 如果没有权限的话则从哪来回哪去

        # 查询category 的信息
        categories = Category.query.all()
        return render_template("release.html", params=locals())
