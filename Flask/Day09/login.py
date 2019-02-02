from flask import Flask, make_response, request, render_template, redirect, session

app = Flask(__name__)
app.config["SECRET_KEY"] = "aixieshaxiesha"


@app.route("/login", methods=["GET", "POST"])
def login():
    method = request.method
    if method == "GET":
        # 获取请求原地址,并保存在session中

        url = request.headers.get("Referer", "/")
        session["url"] = url
        loginstatus = session.get("uname")
        if loginstatus:
            return redirect(url)
        else:
            # cookies中有uname,从cookie中获取uname的值
            uname = request.cookies.get("uname")
            upwd = request.cookies.get("upwd")
            if uname:
                print(uname == "admin" and upwd == "admin")
                if uname == "admin" and upwd == "admin":
                    session["uname"] = uname
                    return redirect(url)
                else:
                    resp = make_response(render_template('login.html'))
                    resp.delete_cookie("uname")
                    resp.delete_cookie("upwd")
                    return resp
            else:
                return render_template('login.html')


    else:
        # 接收登录信息
        uname = request.form.get("uname")
        upwd = request.form.get("upwd")
        isSaved = request.form.get("isSaved")
        if uname == "admin" and upwd == "admin":
            # 将登录信息保存进session 以便让服务器记住登录状态
            session["uname"] = uname
            url = session["url"]
            resp = redirect(url)

            if isSaved == "on":

                resp.set_cookie('uname', uname, 60 * 60 * 24 * 365)
                resp.set_cookie('upwd', upwd, 60 * 60 * 24 * 365)
                return resp
            else:
                return resp



        else:
            return render_template('login.html')


@app.route("/")
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
