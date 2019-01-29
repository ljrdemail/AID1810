from flask import Flask
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


# 创建实体类-Users,映射到数据库中叫users表
# 创建字段id,主键,自增
# 创建字段username,长度为80的字符串,不允许为空,值唯一,加索引
# 创建字段age,整数,允许为空
# 创建字段email,长度为120的字符串,必须唯一
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


class Course(db.Model):
    # 省略__tablename__,默认映射的表名就是将类变成全小写
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)


class Wife(db.Model):
    __tablename__ = 'wife'
    id = db.Column(db.Integer, primary_key=True)
    wname = db.Column(db.String(30), nullable=False)
    wage = db.Column(db.Integer)


# db.drop_all():删除数据库中创建好的所有的数据表
# db.drop_all()

# db.create_all():将创建好的实体类映射回数据库,生成表
# db.create_all()


@app.route('/')
def hello_world():
    return '这是主页！'


@app.route('/01-add')
def add_views():
    # 1.创建Users的对象,并为各个属性赋值
    user = Users()
    user.username = "Rap Wang"
    user.age = 41
    user.email = "rapwang@163.com"
    # 2.将Users的对象通过db.session.add()保存回DB
    db.session.add(user)
    # 3.手动提交操作回数据库
    # db.session.commit()
    return "<h1>提交数据成功!</h1>"


# 访问路径: localhost:5000/02-query
# 目的: 验证db.session.query()的结果
@app.route('/02-query')
def query_views():
    # 1.查询Users实体类中的id,username,age 三个列
    # query = db.session.query(Users.id,Users.username,Users.age)
    # 2.查询Users,Wife实体类中所有的列
    query = db.session.query(Users, Wife)
    print(query)
    print(type(query))
    return "Query OK"


# localhost:5000/03-query
# 目的:在db.session.query()的基础上的到查询结果
@app.route('/03-query')
def query03_views():
    # 1.查询users表中所有的数据
    users = db.session.query(Users).all()
    for u in users:
        print("姓名:%s,年龄:%s,邮箱:%s" % (u.username, u.age, u.email))
    # print(users)
    # print(type(users))
    return "Query OK"


@app.route('/06-filter')
# 目的 解决filter 的用法以及返回量
def filter_views():
    # 1 查询users表中年龄>17 的人的信息
    # result=db.session.query(Users).filter(Users.age>17).filter(Users.id>1)
    # print(result)
    # print(type(result))
    # 2 查询Users实体中年龄大于17岁 并且id 大于1 的Users的信息
    # result = db.session.query(Users).filter(Users.age > 17, Users.id > 1).all()
    # for user in result:
    #     print("ID:%s,姓名:%s,年龄:%s" % (user.id, user.username, user.age))
    # 3 查询年龄大于17 或者id>1 的信息
    users = db.session.query(Users).filter(or_(Users.age > 17, Users.age > 1)).all()
    #     # for user in users:
    #     #     print("ID:%s,姓名:%s,年龄:%s" % (user.id, user.username, user.age))
    # 4查询出id为5 的数据
    # user = db.session.query(Users).filter(Users.id==5).first()
    # 5 查询出username 包含wang 的用户的信息
    # users=db.session.query(Users).filter(Users.username.like("%wang%")).all()
    # 6 查询出username 以 ru结尾的用户的信息
    # users = db.session.query(Users).filter(Users.username.like("%ru")).all()
    # 7 查询出username 以 na开头的用户的信息
    # users = db.session.query(Users).filter(Users.username.like("na%")).all()
    # 8 查询users 表中年龄为 17 30 45 的用户的信息
    # users = db.session.query(Users).filter(Users.age.in_([17, 30, 45])).all()
    # 9 查询users 表中年龄为 在30~45 之间的用户的信息
    users = db.session.query(Users).filter(Users.age.between(30, 45)).all()
    for user in users:
        print("ID:%s,姓名:%s,年龄:%s" % (user.id, user.username, user.age))

    return "QueryOK"


if __name__ == '__main__':
    # 通过 manager 管理对象启动服务
    # 通过 python3 FlaskDemo05.py runserver
    # 问题1:无法指定调试模式 (debug=True)
    # 解决方案:app.config['DEBUG']=True
    # 问题2:无法指定启动端口 (port=5555)
    # 解决方案:python3 xxx.py runserver --port 5555
    # 问题3:无法指定主机地址 (host=0.0.0.0)
    # 解决方案:python3 xxx.py runserver --host 0.0.0.0
    # 问题2,3的解决方案:
    # python3 xxx.py runserver --host 0.0.0.0 --port 5555
    manager.run()
