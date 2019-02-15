# 处理与博客相关的路由和视图
from . import main
from flask import render_template, session, request, redirect
from ..models import *
from .. import db
import datetime
import os


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
    else:
        title = request.form.get("author")
        blogtype = request.form.get("list")
        category = request.form.get("category")
        content = request.form.get("content")
        dest = ""
        userid = session.get("id")

        if request.files:
            try:
                image = request.files["image"]
                ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                ext = image.filename.split(".")[-1]
                filename = ftime + "." + ext
                basedir = os.path.dirname(__file__)
                # uploadpath = os.path.join(basedir, "..\\", "static", "upload", filename) 我的版本
                currentpath = os.path.dirname(os.path.dirname(__file__))  # 老师版本 得到app这一层 然后自己拼static upload
                uploadpath = os.path.join(currentpath, "static", "upload", filename)
                image.save(uploadpath)
                dest = "/upload/" + filename
            except Exception as e:
                print(e)
                return "上传失败！"
        topic = Topic()
        topic.title = title
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        topic.content = content
        topic.images = dest
        topic.blogtype_id = blogtype
        topic.category_id = category
        topic.user_id = userid
        db.session.add(topic)
        db.session.commit()
        return redirect("/")
