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


class Provinces(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80))

    # 关联属性和反向关联属性
    cities = db.relationship(
        "Citys",
        backref="provinces",
        lazy="dynamic"

    )

    def to_dict(self):
        dic = {"id": self.id, "pname": self.pname}
        return dic


class Citys(db.Model):
    __tablename__ = "citys"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(80))
    pid = db.Column(db.Integer, db.ForeignKey("provinces.id"), nullable=True)  # provinces注意是表名不是类名

    def to_dict(self):
        dic = {"id": self.id, "cname": self.cname, "pid": self.pid}
        return dic


db.create_all()


@app.route("/02-province")
def province_views():
    provinces = Provinces.query.all()
    l = []
    for pro in provinces:
        l.append(pro.to_dict())
    return json.dumps(l)


@app.route("/02-city")
def city_views():
    # 先获取前端传递过来的省份ID
    print("我被调用")
    pid = request.args.get("pid")
    print(pid)
    # 根据pid 获取对应的city 的信息
    cities = Citys.query.filter_by(pid=pid).all()
    l = []
    for city in cities:
        l.append(city.to_dict())
    return json.dumps(l)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
