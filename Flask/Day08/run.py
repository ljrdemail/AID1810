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
    # 实现与Teaqcher 的关联关系(多对多，中间借助
    # student_teacher关联表进行关联)
    teachers = db.relationship(
        "Teacher",  # teachers每条记录都是Teacher类
        secondary="student_teacher",  # 经过那张表中转
        lazy="dynamic",  # student 对teacher 也要dynamic
        backref=db.backref("students",  # teacher如何访问student
                           lazy="dynamic")  # teacher 对student 也要dynamic

    )


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


# 声明一个实体类 表示关联student 和teacher 的第三张表
class StudentTeacher(db.Model):
    __tablename__ = "student_teacher"
    id = db.Column(db.Integer, primary_key=True)
    # 外键teacher_id 引用自teacher.id
    teacher_id = db.Column(db.Integer, db.ForeignKey("teacher.id"))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    # 外键 student_id 引用自student.id


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


# 多对多增加关联数据的实现
@app.route("/06-mtm")
def mtm_views():
    # 创建学员对象
    stu = Student()
    stu.sname = "漩涡鸣人"
    stu.sage = 17
    db.session.add(stu)
    db.session.commit()
    # 查询出id 为4 的老师的信息
    tea = Teacher.query.filter_by(id=4).first()
    stu.teachers.append(tea)
    return "插入关联数据成功！"


# 07-mtm-exer
# 目的 多对多增加练习
@app.route("/07-mtm-exer", methods=["GET", "POST"])
def mtm_exer():
    if request.method == "GET":
        teachers = Teacher.query.all()
        return render_template("Day08_02 MTM.html", teachers=teachers)
    else:
        sname = request.form.get("sname")
        sage = request.form.get("sage")
        stu = Student()
        stu.sname = sname
        stu.sage = sage
        db.session.add(stu)
        db.session.commit()
        # 获取所有的teachers的值
        teachers = request.form.getlist("teachers")
        # 获取到有关teachers的所有数据
        list = db.session.query(Teacher).filter(Teacher.id.in_(teachers)).all()
        # 循环遍历list得到每个teacher,append到stu中
        for tea in list:
            stu.teachers.append(tea)
        return "注册成功"


if __name__ == '__main__':
    manager.run()
