from flask import Flask, request, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
# 设置连库字符串
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/flask"
# 设置数据库的信号追踪 会把你所有操作记录（操作日志） 浪费资源内存硬盘 所以关掉
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 设置执行完视图函数后自动提交操作回数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 设置程序的启动模式为调试模式
app.config['DEBUG'] = True
# 创建db对象
db = SQLAlchemy(app)

# 创建Manager对象并指定要管理哪个应用(app)
manager = Manager(app)
# 创建Migrate对象,并指定关联的app和db
migrate = Migrate(app, db)

# 为manager增加命令,允许做数据库的迁移操作
# 为manager绑定一个叫 db 的子命令,该子命令执行操作由MigrateCommand来提供
# migrate = Migrate(app, db) 不能省因为 MigrateCommand 需要用到
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    # 增加字段 isActive,表示用户是否被激活,布尔类型,默认为True
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User:%r>" % self.username


@app.route("/07-filter-exer", methods=["GET", "POST"])
def searchUser():
    users = db.session.query(Users).all()
    method = request.method
    if method == "GET":
        return render_template("Day06_03-SerchView.html", users=users)
    if method == "POST":
        # 接收前端传递过来的kw参数,如果没有则为''
        keywords = request.form.get("keywords")
        print("keywords is " + keywords)
        users = db.session.query(Users).filter(
            or_(Users.username.like("%" + keywords + "%"), Users.email.like("%" + keywords + "%"))).all()

        # 如果kw为空的话,则查询Users中所有数据
        # 如果kw非空的话,则按照条件筛选(username或email中包含kw的就筛选出来)
        # if kw:
        #     # 非空
        #     users = db.session.query(Users).filter(
        #         or_(
        #             Users.username.like("%" + kw + "%"),
        #             Users.email.like("%" + kw + "%")
        #         )
        #     ).all()
        # else:
        #     # 为空
        #     users = db.session.query(Users).all()

        return render_template("Day06_03-SerchView.html", users=users)


if __name__ == '__main__':
    manager.run()
