from flask import Flask, make_response, request, render_template, redirect

app = Flask(__name__)


# 目的设置cookie的值到浏览器中
@app.route("/01-setcookie")
def setcookie_views():
    # 先创建响应对象 -"添加相应对象成功"
    resp = make_response("添加cookie成功")  # 如果你是响应template render_template("***.html")
    # 向cookie 中添加数据key :uname value:wangwc 存期1年
    resp.set_cookie('uname', 'wangwc', 60 * 60 * 24 * 365)
    return resp


# 02-getcookie
# 目的从cookie中取出uname的值

@app.route('/02-getcookie')
def getcookie():
    print(request.cookies)
    uname = request.cookies.get("uname")
    print("uname的值为：" + uname)
    return "获取cookie的值成功"


# 03-delcookie
# 目的从cookie中删除uname的值
@app.route('/03-delcookie')
def delcookie():
    # 删除uname的值
    resp = make_response("删除cookie成功！")
    if "uname" in request.cookies:
        resp.delete_cookie("uname")
    return resp


@app.route("/homework", methods=["GET", "POST"])
def homework():
    method = request.method
    resp = make_response("登录成功")
    if method == "GET":
        uname = request.cookies.get("uname")
        if uname:
            return redirect("/index")
        else:
            return render_template("Day08_01-cookieexec.html")
    else:
        uname = request.form.get("uname")
        passwd = request.form.get("passwd")
        isselect = request.form.get("isselect")

        if isselect == "on":
            print("......")
            resp.set_cookie('uname', uname, 60 * 60 * 24 * 365)

        if uname == "admin" and passwd == "admin":
            return redirect("/index")
        else:
            return redirect("/homework")

    return resp


@app.route("/index")
def backtoindex():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
