from flask import Flask, request
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash

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
        print(uname, pwd)
        return ""


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

        print(username, email, url, password)
        return ""



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
