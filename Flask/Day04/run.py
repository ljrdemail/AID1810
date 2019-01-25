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
            uimg.save("static/" + uimg.filename)
        except Exception as e:
            print(e)
            return "上传失败！"
    return "上传文件成功"


if __name__ == "__main__":
    app.run(debug=True)
