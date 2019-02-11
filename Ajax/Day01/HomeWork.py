from flask import Flask, request, render_template
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/flask"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

app.config['DEBUG'] = True

db = SQLAlchemy(app)

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class User(db.Model):
    __table__name = "users"


@app.route('/')
def index():
    return "Hello World"


@app.route("/register", methods=["POST"])
def register():
    pass


if __name__ == "__main__":
    app.run(debug=True)
