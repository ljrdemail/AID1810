# 根据数据库编写实体类
from . import db


# 创建实体类
# 创建BlogType实体类 ->blogtype
class BlogType(db.Model):
    __tablename__ = "blogtype"
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)
    topics = db.relationship("Topic", backref="blogtype", lazy="dynamic")


# 创建Category实体类 ->category
class Category(db.Model):
    __tablename__ = "category"
    id = db.Column(db.Integer, primary_key=True)
    cate_name = db.Column(db.String(50), nullable=False)
    topics = db.relationship("Topic", backref="category", lazy="dynamic")


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    loginname = db.Column(db.String(50), nullable=False)
    uname = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(200), default="NULL")
    upwd = db.Column(db.String(30), nullable=False)
    is_author = db.Column(db.Integer, default=0)
    topics = db.relationship("Topic", backref="user", lazy="dynamic")
    replys = db.relationship("Reply", backref="user", lazy="dynamic")
    vokes = db.relationship("Voke", backref="user", lazy="dynamic")


class Topic(db.Model):
    __tablename__ = "topic"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    # pub_date = db.Column(db.DateTime, nullable=False)
    read_num = db.Column(db.Integer, default="NULL")
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.Text)
    blogtype_id = db.Column(db.Integer, db.ForeignKey("blogtype.id"), default="NULL")
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), default="NULL")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), default="NULL")
    vokes = db.relationship("Voke", backref="topic", lazy="dynamic")
    replay = db.relationship("Reply", backref="topic", uselist=False)


class Reply(db.Model):
    __tablename__ = "reply"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, autoincrement=True)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
    content = db.Column(db.Text, nullable=False)
    # reply_time = db.Column(db.Datetime, default="NULL")


class Voke(db.Model):
    __tablename__ = "voke"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    topic_id = db.Column(db.Integer, db.ForeignKey("topic.id"), nullable=False)
