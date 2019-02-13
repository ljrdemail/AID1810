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


@app.route('/05-server', methods=['POST', "GET"])
def server05_views():
    # return "成功获取ajax请求" # 无法处理跨域
    # return "console.log('成功获取ajax请求')" #可以处理跨域 但是只能打印
    # 如果想服务器只传数据，在前端通过传JS 来处理后台传过来的数据 通过后端回传JS 调用process_resp
    # return "process_resp('成功获取ajax请求2');"
    # 如果process_resp 不想写死为process_resp
    # 处理方法叫什么通过前台传过来
    callbackfunc = request.args.get("callback")
    return callbackfunc + "('成功获取ajax请求3');"


if __name__ == '__main__':
    app.run(debug=True)
