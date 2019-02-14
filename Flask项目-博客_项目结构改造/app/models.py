# 根据数据库编写实体类
from . import db


# 创建实体类
# 创建BlogType实体类 ->blogtype
class BlogType(db.Model):
    __tablename__ = "blogtype"
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)


# 创建Category实体类 ->category
class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)

# class Topic(db.Model):
#     __tablename__ = "topic"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     pub_date = db.Column(db.datetime, nullable=False)
#     read_num = db.Column(db.Integer(11), default="NULL")
