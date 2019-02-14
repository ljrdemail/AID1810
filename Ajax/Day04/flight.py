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


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/01-flight")
def flights_view():
    # 接收前端传递过来的函数名
    cb = request.args.get("callback")
    # 准备数据
    dic = {"flightNo": "MH370", "from": "KLIA", "to": "PEK", "time": "6:30"}
    jsonStr = json.dumps(dic)
    return cb + "(" + jsonStr + ");"  # 不用发JS过去 由于客户端是用 $.ajax 且为jsonp 类型 会有函数自动处理 你只需要发数据过去就好


# 因为jsonStr没有“” 传递前端是一个对象而不是字符串 不需要在前端parse 如果“jsonStr”就要转


if __name__ == '__main__':
    app.run(debug=True)
