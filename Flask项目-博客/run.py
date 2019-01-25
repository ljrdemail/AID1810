from flask import Flask, request
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash

# generate_password_hash 加密
# check_password_hash 解密
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/list")
def list():
    return render_template('list.html')


@app.route("/login", methods=["POST", "GET"])
def longin():
    method = request.method
    if method == "GET":
        return render_template("/login.html")
    else:
        uname = request.form.get("username")
        pwd = request.form.get("password")
        pwd2 = generate_password_hash(pwd)
        print(uname, pwd, pwd2)
        return "接收数据成功"


@app.route("/register", methods=["POST", "GET"])
def register():
    method = request.method
    if method == "GET":
        return render_template("/register.html")
    else:
        username = request.form.get("username")
        email = request.form.get("email")
        url = request.form.get("url")
        password = request.form.get("password")
        password2 = generate_password_hash(password)
        print(username, email, url, password, password2)
        # 测试加密字符串和原始字符串是否相同
        # password2 从注册时候保存在数据库中的拿出来 password 输入的 就可比对
        print(check_password_hash(password2, password))
        return "接收数据成功"



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
