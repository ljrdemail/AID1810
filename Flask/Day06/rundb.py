import math

from flask import Flask, render_template, request
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


# localhost:5000/06-filter
# 目的:解决filter的用法以及返回值
@app.route('/06-filter')
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
    # users = db.session.query(Users).filter(Users.age.between(30, 45)).all()

    # 10 查询Users实体中isActive为True的信息

    users = db.session.query(Users).filter_by(isActive=True).all()
    for user in users:
        print("ID:%s,姓名:%s,年龄:%s" % (user.id, user.username, user.age))

    return "QueryOK"


# localhost:5000/08-offset
# 目的:练习offset() & limit()
@app.route('/08-offset_limit')
def offset_limit():
    users = db.session.query(Users).offset(3).limit(5)  # limit 和 offset 谁在前都可以
    for user in users:
        print("ID:%s,姓名:%s,年龄:%s" % (user.id, user.username, user.age))

    return "QueryOK"


# localhsot:5000/09-page
# 目的:通过offset() 和 limit() 实现分页查询
# 默认每页只显示2条数据
@app.route("/09-page")
def page_views():
    # 变量-pageSize,表示每页所显示的记录数
    page_size = 2
    # 接收前端传递过来的请求参数-page,如果没有设置为1,保存在变量 page 中
    page = int(request.args.get("page", "1"))
    # print("当前向查看的页数是%d页" %page)
    # 跳过(page-1)*pageSize条数据，再获取前pageSize条
    # 通过pageSize和总记录数计算尾页的页码
    # 变量totolCount,表示Users中的总记录数
    totalCount = db.session.query(Users).count()
    # 变量lastPage 用于表示计算出来的尾页页码
    lastPage = math.ceil(totalCount / page_size)
    # print("总页数为%d页" %lastPage)
    # 通过page计算上一页的页码 下一页的页码
    # 变量prevPage 用于表示上一页的页码
    prevPage = 1
    if page > 1:
        prevPage = page - 1

    # nextPage 用于表示下一页的页码
    nextPage = lastPage
    if page < lastPage:
        nextPage = page + 1

    users = db.session.query(Users).limit(page_size).offset((page - 1) * page_size).all()  # 首页
    return render_template("Day06_04-FenYe.html", users=users, prevPage=prevPage, nextPage=nextPage, lastPage=lastPage)


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
