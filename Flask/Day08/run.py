from flask import Flask, request, render_template
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
    # 增加属性:关联属性,针对Wife表的一对一关系的关联属性和反向引用关系属性
    wife = db.relationship(
        "Wife",
        backref="user",
        uselist=False  # 告诉系统是对象不是列表 因为一对一
    )

    def __repr__(self):
        return "<User:%r>" % self.username


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, nullable=False, default=True)


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)
    # 准备增加对Course（一）的外键引用
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=True)  # 是表名不是类名


class Course(db.Model):
    # 省略__tablename__,默认映射的表名就是将类变成全小写
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)
    # 增加关联属性和反向引用关系属性
    teachers = db.relationship(  # 在Couse中通过teachers 找到所有能教这门课的teacher
        "Teacher", backref="course",  # 在Teacher中通过course来找到对应的Course
        lazy="dynamic"
    )


class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30), nullable=False)
    wage = db.Column(db.Integer)
    # 增加外键,引用自 users表的主键id(一对一)
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id'),
        unique=True,
        nullable=True
    )


# localhost:5000/01-oto
# 目的:实现一对一增加数据操作
@app.route('/01-oto')
def oto_views():
    # 1. 通过外键(user_id)添加关联信息
    # wife = Wife()
    # wife.wname = "王夫人"
    # wife.wage = 18
    # wife.user_id = 1
    # db.session.add(wife)
    # 2. 通过反向引用关系属性添加关联信息
    user = Users.query.filter_by(id=6).first()
    wife = Wife()
    wife.wname = "Rap Wang 的夫人"
    wife.wage = 30
    wife.user = user
    db.session.add(wife)
    return "Register wife OK"


# localhost:5000/02-oto-exer
# 目的:一对一增加练习以及业务处理
@app.route('/02-oto-exer', methods=['GET', 'POST'])
def oto_exer():
    if request.method == 'GET':
        users = Users.query.all()
        return render_template('05-oto-exer.html', users=users)
    else:
        # 接收前端传递过来的数据
        wname = request.form['wname']
        wage = request.form['wage']
        user_id = request.form['user']
        # 判断user_id在wife表中是否存在(查询wife表中是否存在user_id=user_id的数据)
        wife = Wife.query.filter_by(user_id=user_id).first()
        if wife:
            # 表示user_id已经存在,给出错误提示
            errMsg = '该User信息已经存在,请重新选择'
            users = Users.query.all()
            return render_template(
                '05-oto-exer.html',
                errMsg=errMsg,
                users=users,
                wname=wname
            )
        else:
            # 表示user_id不存在,可以正常插入
            wife = Wife()
            wife.wname = wname
            wife.wage = wage
            wife.user_id = user_id
            db.session.add(wife)
            return "Wife注册成功"


if __name__ == '__main__':
    manager.run()
