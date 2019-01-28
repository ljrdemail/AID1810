import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@127.0.0.1:3306/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# 创建实体类-Users 映射到数据库中的叫 users 表
# 创建字段id,主键，自增
# 创建字段username,长度为80的字符串 不允许为空值唯一，加索引
# 创建字段edge 整数允许为空
# 创建字段email 长度为120的字符串 必须唯一


class User(db.Model):
    __table__name = "USERS"
    id = db.Column(db.Integer, primary_key=True)  # autoincrement 默认就是True 不用设定
    username = db.Column(db.String(80), nullable=False, unique=True, index=True)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(120), unique=True)
    # 增加字段 isActive  表示用户是否被激活 布尔类型 默认为True 不能修改必须先删除该表之后重新创建
    isActive = db.Column(db.Boolean, default=True)


class Student(db.Model):
    __table__name = "student"
    id = db.Column(db.Integer, primary_key=True)
    sname = db.Column(db.String(30), nullable=False)
    sage = db.Column(db.Integer, nullable=False)
    isActive = db.Column(db.Boolean, default=True, nullable=False)


class Teacer(db.Model):
    __table__name = "teacher"  # 如果省略按照类名首字母小写创建表名
    id = db.Column(db.Integer, primary_key=True)
    tname = db.Column(db.String(30), nullable=False)
    tage = db.Column(db.Integer, nullable=False)


class Course(db.Model):
    __table__name = 'course'
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(30), nullable=False)


__table__name = "course"
id = db.Column(db.Integer, primary_key=True)

# 将所有表删除
db.drop_all()

# db.create_all()将创建好的实体类映射会数据库，生成表
db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
