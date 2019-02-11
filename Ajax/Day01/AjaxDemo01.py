from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route("/01-server")
def server01():
    # return "这是我的第一个AJAX请求"+100 #引起500错误
    return "这是我的第一个AJAX请求"


@app.route("/02-server")
def server02():
    uname = request.args.get("uname")
    return "欢迎：" + uname


if __name__ == "__main__":
    app.run(debug=True)
