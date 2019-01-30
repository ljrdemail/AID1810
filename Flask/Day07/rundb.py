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
    # Users实体中,按isActive分组后每组人数
    result3 = db.session.query(Users.isActive, func.count('*')).group_by('isActive').all()
    # 1 查询总年龄
    result4 = db.session.query(func.sum(Users.age)).all()
    # 2 查询总人数
    result5 = db.session.query(func.count(Users.id)).all()
    # 3 查询users表中所有人的平均年龄是多少
    result6 = db.session.query(func.avg(Users.age)).all()
    # 4 查询users 表中年龄大于18岁的人的平均年龄是多少
    result7 = db.session.query(func.avg(Users.age)).filter(Users.age > 18).all()
    # 5 查询users表中按 isactive分组后 每组的人数是多少
    result8 = db.session.query(Users.isActive, func.count(Users.id)).group_by("isActive").all()
    # 6 查询users表中按 isactive分组后 组内人数大于2人的组的人数
    result9 = db.session.query(Users.isActive, func.count(Users.id)).group_by("isActive").having(
        func.count(Users.id) > 2).all()
    # 7 查询users表中年龄大于18岁的人按isactive分组后 组内人数大于2人的组的信息
    result10 = db.session.query(Users.isActive, func.count(Users.id)).filter(Users.age > 18).group_by(
        "isActive").having(
        func.count(Users.id) > 2).all()
    print("平均年龄为:%.2f" % result[0])
    print("平均年龄为:%.2f,总年龄为：%.2f,最大年龄为：%.2f,最小年龄为:%.2f" % (result2[0][0], result2[0][1], result2[0][2], result2[0][3]))
    print("总年龄为：%d" % result4[0])
    print(result10)

    return "QueryOK"


@app.route("/02-update")
def update():
    user = db.session.query(Users).filter_by(id=5).first()
    user.age = 38;
    db.session.add(user)
    return "Update OK"


@app.route("/02-updatelist")
def updatelist():
    users = db.session.query(Users).filter(Users.username.like("%panpan%")).all()
    for u in users:
        u.age = 38;
        db.session.add(u)
    return "Updatelist OK"


@app.route("/03-delete")
def delete():
    user = db.session.query(Users).filter_by(id=5).first()
    db.session.delete(user)
    db.session.commit()
    return "delete OK"


@app.route("/04-deletelist")
def deletelist():
    users = db.session.query(Users).filter(Users.username.like("%panpan%")).all()
    for u in users:
        db.session.delete(u)
    db.session.commit()
    return "deletelist OK"


if __name__ == '__main__':
    manager.run()
