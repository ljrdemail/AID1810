import datetime
import os

from flask import Flask, request, render_template

app = Flask(__name__)


# 测试getlist方法
@app.route("/01-form", methods=['GET', 'POST'])
def form_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_01-form.html")
    elif method == "POST":
        uname = request.form.get("uname")
        hobby = request.form.getlist("hobby")
        country = request.form.getlist("country")
        print(uname, hobby, country)
        return "接收数据成功"


# 目的 文件上传
@app.route("/02-file", methods=["GET", "POST"])
def file_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_02-file.html")
    else:
        # 接收数据
        uname = request.form.get("uname")
        uimg = request.files['uimg']  # uimg是一个文件 传入'uimg' 用于传入name=uimg的那个文本框
        # 保存数据 相对路径satic中
        try:
            # 以上传的时间来作为上传的文件名-避免上传的资源重复
            # 格式 YYYYMMDDHHMMSSFFFFFF.扩展名
            # 根据时间平街层名称字符串
            # 根据原有的文件名获取扩展名
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            houzhui = uimg.filename.split(".")[-1]
            houzhui2 = uimg.filename[uimg.filename.index(".") + 1::]

            # 拼接
            # filename=ftime+"."+houzhui
            filename = ftime + "." + houzhui2
            # uimg.save("static/" + filename)
            # 使用绝对路径
            basedir = os.path.dirname(__file__)  # run.py所在的路径
            # 拼接完整路径
            uploadpath = os.path.join(basedir, "static", filename)
            uimg.save(uploadpath)
        except Exception as e:
            print(e)
            return "上传失败！"
    return "上传文件成功"


@app.route("/03-release", methods=["GET", "POST"])
def release_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_03-release.html")
    else:
        blogtitle = request.form.get("blogtitle")
        blogtype = request.form.getlist("blogtype")
        blogimg = request.files.get("blogimg")
        blogcontent = request.form.get("blogcontent")
        print(blogtitle, blogtype, blogcontent)
        if blogimg != None:
            basedir = os.path.dirname(__file__)
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            houzhui = blogimg.filename.split(".")[-1]
            filename = ftime + "." + houzhui
            uploaddir = os.path.join(basedir, "static", "upload", filename)
            blogimg.save(uploaddir)
    return "上传成功！"


if __name__ == "__main__":
    app.run(debug=True)
