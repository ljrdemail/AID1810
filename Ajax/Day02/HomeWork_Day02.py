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


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, index=True)
    password = db.Column(db.String(100))
    email = db.Column(db.String(120))
    isActive = db.Column(db.Boolean, default=True)

    def to_dict(self):
        dic = {"id": self.id, "uname": self.username, "upwd": self.password, "uemail": self.email,
               "uisActicve": self.isActive}
        return dic


@app.route('/')
def index():
    return "Hello World"


@app.route("/listuser")
def list_user():
    uname = request.args.get("uname")
    print("uname:" + uname)
    users = db.session.query(Users).filter(Users.username.like("%" + uname + "%")).all()
    l = []
    for u in users:
        l.append(u.to_dict())
    if uname == "":
        return json.dumps("")
    else:
        return json.dumps(l)


if __name__ == "__main__":
    manager.run()
