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


# 目的 关联数据的插入 增加teacher时同时制定对应的 course
@app.route("/01-regtea")
def regtea_views():
    # 声明一个teacher 的对象 通过course_id属性类关联对应的course
    tea = Teacher()
    tea.tname = "魏明择"
    tea.tage = 40
    tea.course_id = 1
    db.session.add(tea)

    # 方案2 声明一个Teacher对象 通过course属性来关联对应的Course(反向引用)
    # 1 获取cname为爬虫的course 对象
    course = Course.query.filter_by(cname="爬虫").first()
    # 2 创建Teacher对象 并关联course 对象
    teacher = Teacher()
    teacher.tname = "王伟超"
    teacher.tage = 37
    teacher.course = course
    # teacher.course_id=course.id #因为你告诉了teacher.course_id ref course.id
    # course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=True)  # 是表名不是类名
    db.session.add(teacher)
    return "Teacher注册成功"


# 目的 一对多 关联属性 反向引用关系的相关查询
@app.route("/02-query")
def query_views():
    # 查询 王伟超老师 的个人信息以及相应的课程信息
    tea = Teacher.query.filter_by(tname="王伟超").first()
    print("tea.course的类型为:", type(tea.course))  # teacher中有course 是因为在关联属性的时候设定进去的
    print("姓名 ：%s ,年龄: %s 所教课程:%s" % (tea.tname, tea.tage, tea.course.cname))

    # 查询爬虫课程以及对应的授课老师
    course = Course.query.filter_by(cname="爬虫").first()
    print("课程名称:" + course.cname)
    teas = course.teachers
    print(type(teas))  # AppenderBaseQuery 是一个query 可以进一步查询
    # course.teachers 是针对course课程的对应的所有授课老师的一个查询对象（并非最终结果）
    for t in teas.all():
        print("老师名称：", t.tname)
        print("老师年龄：", t.tage)
    return "Query OK"


@app.route("/03-exec")
def queryexer_views():
    # 查询Course实体中所有的数据
    courses = Course.query.all()

    # 接收前端传递过来的cid的值
    # 有cid参数,则查询对应的课程的老师
    # 没有cid参数,则查询所有老师
    if 'cid' in request.args:
        cid = request.args['cid']
        # 先查询出cid对应的课程
        course = Course.query.filter_by(id=cid).first()
        # 再查询课程对应的老师们
        teachers = course.teachers.all()
    else:
        cid = "0"
        teachers = Teacher.query.all()

    return render_template('Day07_01-teachers.html', courses=courses, teachers=teachers, cid=int(cid))



if __name__ == '__main__':
    manager.run()
