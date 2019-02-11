from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route("/03-server", methods=["POST"])
def server03():
    uname = request.form.get("uname")
    upwd = request.form.get("upwd")
    print(uname, upwd)

    return "用户名:" + uname + "，密码:" + upwd


if __name__ == "__main__":
    app.run(debug=True)
