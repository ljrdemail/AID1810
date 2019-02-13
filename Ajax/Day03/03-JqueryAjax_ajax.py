from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
# 指定数据库的连接配置
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/ajax"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# 创建数据库实例
db = SQLAlchemy(app)


# 创建实体类
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(
        db.Integer, primary_key=True
    )
    uname = db.Column(
        db.String(50), nullable=False, unique=True
    )
    upwd = db.Column(
        db.String(50), nullable=False
    )
    uemail = db.Column(
        db.String(200), nullable=True
    )

    def to_dict(self):
        dic = {"id": self.id, "uname": self.uname, "upwd": self.upwd, "uemail": self.uemail}
        return dic


@app.route('/')
def index():
    return "Hello World"


@app.route('/02-post', methods=['POST', "GET"])
def register_views():
    print("被调用")
    uname = request.form['uname']
    upwd = request.form['upwd']
    uemail = request.form['uemail']
    user = User()
    user.uname = uname
    user.upwd = upwd
    user.uemail = uemail

    try:
        db.session.add(user)
        db.session.commit()
        return "注册成功!"
    except Exception as ex:
        print(ex)
        return "注册失败,请联系管理员!"


if __name__ == '__main__':
    app.run(debug=True)
