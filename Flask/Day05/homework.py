from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/flask"
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
    username = db.Column(
        db.String(80), unique=True, index=True
    )
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(
        db.String(120), unique=True
    )
    isActive = db.Column(db.Boolean, default=True)


@app.route("/04-register", methods=["GET", "POST"])
def register_views():
    method = request.method
    if method == "GET":
        return render_template("Day05_01-register.html")
    else:
        # 声明一个变量 status 用来表示提交数据的状态
        status = 1
        # 接收请求提交的数据
        username = request.form['username']
        age = request.form['age']
        email = request.form['email']
        user = Users()
        user.username = username
        user.age = age
        user.email = email
        try:
            db.session.add(user)
            db.session.commit()  # 9.55

        except  Exception as ex:
            print(ex)
            print("出错了")
            # 将status 修改为0 表示插入数据失败
            status = 0
        finally:
            if status == 1:
                # return "<a href='#'>查看所有</a>"
                # 通过重定向的手段跳转的到queryall 的页面
                return redirect("/05-queryall")
            else:
                return "<h2>您的权限不够，请联系管理员....</h2>"


@app.route("/05-queryall")
def queryall_views():
    users = db.session.query(Users).all()
    return render_template("Day05_02-queryall.html", users=users)


if __name__ == '__main__':
    manager.run()
