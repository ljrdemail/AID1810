from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand


# generate_password_hash 加密
# check_password_hash 解密
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/blog"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


# 创建实体类
class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(30), nullable=False
    )
    email = db.Column(
        db.String(200), nullable=True
    )
    url = db.Column(
        db.String(200), nullable=True
    )
    upwd = db.Column(
        db.String(200), nullable=False
    )

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
        # 加密后的字符串从注册时候保存在数据库中拿出来 rawpassword 从界面传入，并比对
        print(check_password_hash(password2, password))
        return "接收数据成功"



if __name__ == "__main__":
    manager.run()
