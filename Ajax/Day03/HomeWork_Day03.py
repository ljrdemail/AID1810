from flask import Flask, request, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/ajax"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['DEBUG'] = True
db = SQLAlchemy(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


class Provinces(db.Model):
    __tablename__ = "provinces"
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(80))

    def to_dict(self):
        dic = {"id": self.id, "pname": self.pname}
        return dic


class Citys(db.Model):
    __tablename__ = "citys"
    id = db.Column(db.Integer, primary_key=True)
    cname = db.Column(db.String(80))
    pid = db.Column(db.Integer, db.ForeignKey("provinces.id"), nullable=True)

    def to_dict(self):
        dic = {"id": self.id, "cname": self.cname}
        return dic


@app.route('/')
def index():
    return "Hello World"


@app.route("/listprovinces")
def list_provinces():
    provinces = db.session.query(Provinces).all()
    l = []
    for p in provinces:
        l.append(p.to_dict())
    return json.dumps(l)


@app.route("/listcitys")
def list_citys():
    pid = request.args.get("pid")
    citys = db.session.query(Citys).filter(Citys.pid == pid).all()
    l = []
    for c in citys:
        l.append(c.to_dict())
    return json.dumps(l)


if __name__ == "__main__":
    manager.run()
