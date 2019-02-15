# 处理与博客相关的路由和视图
from . import main
from flask import render_template, session, request
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
        if request.files:
            try:
                image = request.files["image"]
                # 以上传的时间来作为上传的文件名-避免上传的资源重复
                # 格式:YYYYMMDDHHMMSSFFFFFF.扩展名
                # 1.根据时间拼成名称字符串
                ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
                # print('时间字符串:%s'%ftime)
                # 2.根据原有的文件名(uimg.filename)获取扩展名
                houzhui = image.filename.split(".")[-1]
                # 3.将ftime.ext拼接到一起
                # filename=ftime+"."+houzhui
                filename = ftime + "." + houzhui
                # uimg.save("static/" + filename)
                # 使用绝对路径上传 /home/tarena/.../static/xx.ext
                basedir = os.path.dirname(__file__)  # 返回 run.py所在的路径

                # 拼完整的保存路径
                uploadpath = os.path.join(basedir, "..\\", "static", "upload", filename)  # 每层目录用逗号分隔
                print(uploadpath)
                image.save(uploadpath)
                dest = "/upload/" + filename

            except Exception as e:
                print(e)
                return "上传失败！"
        print(dest)
        topic = Topic()
        topic.title = title
        topic.pub_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        topic.content = content
        topic.images = dest
        topic.blogtype_id = blogtype
        topic.category_id = category
        db.session.add(topic)
        db.session.commit()
        return "保存成功"
