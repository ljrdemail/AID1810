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
    # 查询出Topic中的所有数据
    topics = Topic.query.all()
    # 判断session中是否有id 和loginname的值
    if "id" in session and "loginname" in session:
        # 已经登录过 从数据库中获取已登录用户的信息 用于在前台显示用户名
        id = session["id"]
        user = User.query.filter_by(ID=id).first()


    return render_template('index.html', params=locals())


@main.route("/release", methods=["GET", "POST"])
def release_views():
    if request.method == "GET":
        # 权限验证,判断是否有用户登录以及登录者的身份是否为作者,如果没有权限的话则从哪来回哪去

        # 判断是否有登录用户
        if 'id' in session and 'loginname' in session:
            # 判断是否有发表博客的权限
            user = User.query.filter_by(ID=session['id']).first()
            if user.is_author:
                # 具备发布博客的权限
                # 查询category 的信息
                categories = Category.query.all()
                return render_template("release.html", params=locals())
        # 没登录从哪里来滚回那里去
        url = request.headers.get('Referer', '/')
        return redirect(url)
    else:
        # post请求处理发表博客的相关操作（保存界面信息）
        # 2.接收前段传递过来的值并赋值给topic
        title = request.form.get("author")
        blogtype = request.form.get("list")
        category = request.form.get("category")
        content = request.form.get("content")
        dest = ""
        userid = session.get("id")
        # 判断是否有文件上传,如果有的话则将文件保存至static/upload,并将文件路径名赋值给topic.images
        if request.files:
            try:
                image = request.files["image"]
                ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                ext = image.filename.split(".")[-1]
                filename = ftime + "." + ext
                basedir = os.path.dirname(__file__)
                # uploadpath = os.path.join(basedir, "..\\", "static", "upload", filename) 我的版本
                # 处理上传路径:upload/xxx.xx
                # 将文件路径赋值给topic.images:upload/xxx.xx
                currentpath = os.path.dirname(os.path.dirname(__file__))  # 老师版本 得到app这一层 然后自己拼static upload
                uploadpath = os.path.join(currentpath, "static", "upload", filename)
                # 将文件保存到指定目录下
                image.save(uploadpath)
                dest = "upload/" + filename
            except Exception as e:
                print(e)
                return "上传失败！"
            # 1.创建Topic对象 - topic
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
