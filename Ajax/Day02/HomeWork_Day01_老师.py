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


db.create_all()  # 没用migrate 所以用create_all


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/01-checkuname')
def checkuname():
    # 接收前端传递过来的uname
    uname = request.args['uname']
    # 验证uname在user表中是否存在
    users = User.query.filter_by(uname=uname).all()
    # 根据验证结果,给出返回值 0 或 1
    if users:
        return "1"
    else:
        return "0"


@app.route('/01-register', methods=['POST'])
def register_views():
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
        return "注册成功"
    except Exception as ex:
        print(ex)
        return "注册失败,请联系管理员"


@app.route('/02-query')
def query_views():
    users = User.query.all()
    # 循环遍历users列表,取出每一块内容再拼成字符串进行响应
    s = ""
    for u in users:
        s += str(u.id) + "-" + u.uname + "-" + u.upwd + "-" + u.uemail
        s += "|"
    # 去掉最后一个 |
    s = s[:-1]
    return s


@app.route("/03-json")
def json_views():
    # 创建字典并转换成JSON字符串 list tuple dict str 都可以序列化字节通过dumps 转换为json字符串
    # dic = {"name": "Uzumaki Naruto", "age": 16, "gender": "Male"}
    # list = [1, 2, 3, 4, 5]
    # tuple = (4, 5, 6, 7, 8)
    # str2 = "ABC"
    # jsonStr = json.dumps(tuple)
    # # jsonStr = json.dumps(list)
    # # jsonStr = json.dumps(tuple)
    # # jsonStr = json.dumps(str2)
    # return jsonStr

    # 查询User表中所有的数据
    users = User.query.all()
    # jsonStr=json.dumps(users) #不能直接把对象放进去 因为user 不能serializable
    # 循环遍历users将每个元素通过to_dict转换成字典再追加到一个列表当中
    list = []
    for u in users:
        list.append(u.to_dict())
    jsonStr = json.dumps(list)
    return jsonStr


if __name__ == '__main__':
    app.run(debug=True)
