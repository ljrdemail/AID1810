from flask import Flask, make_response, request, render_template, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "aixieshaxiesha"


@app.route("/01-setsession")
def setsession():
    session["uname"] = "wangwc"
    return "保存session成功"


@app.route("/02-getsession")
def getsession():
    if "uname" in session:
        uname = session.get("uname")
        return "你存储的值为:" + uname
    else:
        return "你的存储空间中没有数据或没有存储空间"


@app.route("/login", methods=["GET", "POST"])
def login():
    method = request.method
    if method == "GET":
        return render_template("Day09_01-login.html")
    else:
        uname = request.form.get("uname")
        upwd = request.form.get("upwd")
        if uname == "admin" and upwd == "admin":
            # 将登录信息保存进session 以便让服务器记住登录状态
            session["uname"] = uname
            return redirect("/")
        else:
            return redirect("Day09_01-login.html", errMsg="用户名或密码错误！")


@app.route("/")
def index():
    if "uname" in session:
        uname = session.get("uname")
        # 从session 中获取uname的值 能获取到证明登录中 获取不到代表不存在登录状态
        return "<h2>欢迎：%s 光临</h2>" % uname
    else:
        return "你没有登录，请先登录！"


if __name__ == '__main__':
    app.run(debug=True)
