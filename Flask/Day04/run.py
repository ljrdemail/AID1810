import datetime
import os

from flask import Flask, request, render_template

app = Flask(__name__)


# localhost:5000/01-form
# 目的:测试getlist方法
@app.route("/01-form", methods=['GET', 'POST'])
def form_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_01-form.html")
    elif method == "POST":
        uname = request.form.get("uname")
        hobby = request.form.getlist("hobby")
        country = request.form.getlist("country")
        print(uname)
        print(hobby)
        print(country)
        return "接收数据成功"


# localhost:5000/02-file
#目的:文件上传
@app.route("/02-file", methods=["GET", "POST"])
def file_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_02-file.html")
    else:
        # 接收数据
        uname = request.form.get("uname")
        uimg = request.files['uimg']  # uimg是一个文件对象 传入'uimg' 为前端的文本框的name 属性
        # 保存uimg到指定目录 - 相对路径 static 目录中
        try:
            # 以上传的时间来作为上传的文件名-避免上传的资源重复
            # 格式:YYYYMMDDHHMMSSFFFFFF.扩展名
            # 1.根据时间拼成名称字符串
            ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # print('时间字符串:%s'%ftime)
            # 2.根据原有的文件名(uimg.filename)获取扩展名
            houzhui = uimg.filename.split(".")[-1]
            houzhui2 = uimg.filename[uimg.filename.index(".") + 1::]

            # 3.将ftime.ext拼接到一起
            # filename=ftime+"."+houzhui
            filename = ftime + "." + houzhui2
            # uimg.save("static/" + filename)
            # 使用绝对路径上传 /home/tarena/.../static/xx.ext
            basedir = os.path.dirname(__file__)  # 返回 run.py所在的路径
            # 拼完整的保存路径
            uploadpath = os.path.join(basedir, "static", filename)  #每层目录用逗号分隔
            uimg.save(uploadpath)
        except Exception as e:
            print(e)
            return "上传失败！"
    return "上传文件成功"


# localhost:5000/03-release
#目的:前后端request综合练习
@app.route("/03-release", methods=["GET", "POST"])
def release_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_03-release.html")
    else:
        # 接收前端传递过来的数据
        blogtitle = request.form.get("blogtitle")
        blogtype = request.form.getlist("blogtype")
        blogcontent = request.form.get("blogcontent")
        print("文章标题:" + blogtitle)
        print("文章类型:" + blogtype)
        print("文章内容:" + blogcontent)
        # 从上传的图片中获取名为blogimg的图片文件
        blogimg = request.files.get("blogimg")
        # 接收上传图片
        # 判断上传的文件们中有没有叫做blogimg的文件
        #if 'picture' in request.files: 老师的写法
        if blogimg != None:
            # 获取上传的绝对路径
            basedir = os.path.dirname(__file__)
            # ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
            # houzhui = blogimg.filename.split(".")[-1]
            # 获取新文件名
            # filename = ftime + "." + houzhui
            filename = generateFileName(blogimg)
            print("生成文件名：", filename)
            # uploaddir = os.path.join(basedir, "static", "upload", filename)
            # 拼接路径和文件名称
            uploaddir = os.path.join(basedir, "static/upload", filename)  # 也可以
            # 保存file
            blogimg.save(uploaddir)
    return "上传成功！"


#### 根据时间和原文件的扩展名生成新的文件名称
#### 参数 fielname:原文件名称
#### 返回值 : 新生成的文件名
def generateFileName(picture):
    # 获取事件字符串
    ftime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    # 获取文件扩展名
    houzhui = picture.filename.split(".")[-1]  # -1 避免如果第一个是空格 所以不用1
    # 拼成新文件名
    filename = ftime + "." + houzhui
    return filename

if __name__ == "__main__":
    app.run(debug=True)
