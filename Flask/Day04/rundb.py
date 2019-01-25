from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import pymysql # 用来替代mysqldb 因为SQLAlchemy 依赖 mysqldb
# pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 为app指定连接字符串
# app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@127.0.0.1:3306/flask" 不加+pymyql 就必须有
# import pymysql # 用来替代mysqldb 因为SQLAlchemy 依赖 mysqldb
# pymysql.install_as_MySQLdb()
# 加了+pymyql 就可以省略导包
# 默认有 SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and 信号追踪 可以设定为false 因为会很耗内存
# 手动关闭

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@127.0.0.1:3306/flask"
# 取消 信号追踪 SQLALCHEMY_TRACK_MODIFICATIONS 必须放在config 和 db=SQLAlchemy(app) 之间
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 创建SQLALchemy 程序实例-db
db = SQLAlchemy(app)

if __name__ == "__main__":
    app.run(debug=True)
