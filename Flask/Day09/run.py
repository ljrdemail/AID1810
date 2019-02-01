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


if __name__ == '__main__':
    app.run(debug=True)
