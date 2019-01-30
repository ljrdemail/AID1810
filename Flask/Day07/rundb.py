from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

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
    username = db.Column(db.String(80), unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    isActive = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return "<User:%r>" % self.username


@app.route("/01-orderby")
def orderby():
    users = db.session.query(Users).filter(Users.age > 18).order_by("age desc ,id").all()
    for user in users:
        print("ID:%s,姓名:%s,年龄:%s" % (user.id, user.username, user.age))

    return "QueryOK"


# 目的实现聚合查询
@app.route("/01-groupby")
def groupby():
    # 查询平均年龄
    result = db.session.query(func.avg(Users.age)).all()
    # 查询Users实体中所有的平均年龄 总年龄 最大年龄 最小年龄分别是多少
    result2 = db.session.query(func.avg(Users.age), func.sum(Users.age), func.max(Users.age), func.min(Users.age)).all()
    result3 = db.session.query(func.count(Users.age)).group_by("isActive").all()
    print(result3)
    print("平均年龄为:%.2f" % result[0])
    print("平均年龄为:%.2f,总年龄为：%.2f,最大年龄为：%.2f,最小年龄为:%.2f" % (result2[0][0], result2[0][1], result2[0][2], result2[0][3]))
    print("记录条数为：%d" % result3[0])
    return "QueryOK"


if __name__ == '__main__':
    manager.run()
