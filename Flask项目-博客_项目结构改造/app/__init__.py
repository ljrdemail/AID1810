# 当前程序的初始化
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 声明 SQLAlchemy的实例
db = SQLAlchemy()  # 放在外面是为了便于别的模块导入db 不用new App 之后返回db


# 1 创建flask 应用(app) 以及各种配置
def create_app():
    # 创建Flask程序示例-App
    app = Flask(__name__)
    # 为app指定各种配置
    app.config['DEBUG'] = True
    # 为app指定数据库相关配置
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/blog"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # 配置session所需要的SECURET_KEY
    app.config["SECURET_KEY"] = "ljrdemail5266790"  # 随便写用于密码加密
    # 关联db 以及 app
    db.init_app(app)  # 指定db 用哪个App初始化
    # 返回创建好的程序实例app

    # 将main蓝图与app 关联到一起 也就是让app 管理main
    from .main import main as main_blurprint  # 这里的main 指的是main=Blueprint("main",__name__)
    app.register_blueprint(main_blurprint)  # 注册给 app

    # 返回创建好的程序实例app
    return app
