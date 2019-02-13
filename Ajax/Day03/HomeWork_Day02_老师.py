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
        db.String(50), nullable=False
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
def hello_world():
    return 'Hello World!'


@app.route("/01-search")
def search_views():
    # 1 接收前端传递过来的用户名称-uname
    uname = request.args.get("uname", "")  # 如果不传 默认是空
    # 2 根据用户名称做模糊查询-like
    if uname != "":
        users = db.session.query(User.uname).filter(User.uname.like("%" + uname + "%")).all()
        # 处理结果
        # users = [('wangwc',),('rap wang',)]
        l = []
        for s in users:
            l.append(s[0])  #每一个数一个元组s[0] 取元组的第一个元素 就是名称
        jsonStr = json.dumps(l)
        # 4 将结果转换为JSON格式字符串进行响应
        jsonStr = json.dumps(l)
        return jsonStr
    else:
        return json.dumps("")



if __name__ == '__main__':
    app.run(debug=True)
