from flask import Flask, request, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/ajax"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['DEBUG'] = True

db = SQLAlchemy(app)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(120))
    isActive = db.Column(db.Boolean, default=True)


@app.route('/')
def index():
    return "Hello World"


@app.route("/user-query", methods=["GET", "POST"])
def user_query():
    uname = request.args.get("uname")
    res = db.session.query(Users.id, func.count('*')).filter(Users.username == uname)
    if res[0][1] == 1:
        return "用户已经存在，请重新输入用户名！"
    else:
        return "用户不存在，可以注册！"


@app.route("/save-user", methods=["GET", "POST"])
def save_user():
    uname = request.form.get("uname")
    upwd = request.form.get("upwd")
    uemail = request.form.get("uemail")
    user = Users()
    user.username = uname
    user.password = upwd
    user.email = uemail
    db.session.add(user)
    return "注册成功"


if __name__ == "__main__":
    manager.run()
