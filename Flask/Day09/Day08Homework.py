from flask import Flask, make_response, request, render_template, redirect

app = Flask(__name__)


@app.route("/")
def index():
    uname = request.cookies.get("uname")
    return render_template("index.html", uname=uname)


@app.route("/login", methods=["GET", "POST"])
def login_views():
    method = request.method
    if method == "GET":
        return render_template("login.html", params={})
    else:
        # 接收用户名称和密码
        uname = request.form.get("uname")
        upwd = request.form.get("upwd")
        errMsg = "用户名或密码不正确！"
        # 验证用户名称和密码的正确性（是否为admin）
        if uname == "admin" and upwd == "admin":
            # 如果正确则继续判断是否有记住密码

            resp = redirect("/")

            if ("isSaved" in request.form):
                # 将uname保存进cookie
                resp.set_cookie('uname', uname, 60 * 60 * 24 * 365)
            return resp

        else:
            # 如果不正确则再回到login.html中
            return render_template("/login.html", params=locals())


@app.route("/logout")
def logout():
    # 获取请求源地址
    url = request.headers.get("Referer", "/")
    # 通过url构建响应对象
    resp = redirect(url)
    # 判断uname是否在cookies中
    if "uname" in request.cookies:
        resp.delete_cookie("uname")
    return resp


if __name__ == '__main__':
    app.run(debug=True)
