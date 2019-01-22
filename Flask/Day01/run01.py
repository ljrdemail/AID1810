# 用于演示FLASK框架的搭建
from flask import Flask

# 将当运行的主程序构建成Flask应用，以便接收用户请求（request）并给出响应(response)
app = Flask(__name__)


# @app.route("/") FLASK中的路由定义，主要匹配用户的访问路径 ‘/’表示的是整个网站的根路径
# def index() 表示匹配上访问路径之后路的处理程序 也就是Java中的action 也就是MTV 中的 V MVC的C  视图处理函数必须要有返回值 这个例子中的返回值是字符串 表示要响应给客户端浏览器的内容 也就是spring 里面的mapping
@app.route('/')  # Flask(__name__)返回值叫啥 @后就叫啥
def index():#不是强制/的必须叫 index 名字随便 是根据route 决定
    return "This is my First flask demo"


@app.route('/abc')  # 必须要有/
def abc():
    return "This is abc application"


if __name__ == "__main__":
    app.run(debug=True)
    # 运行Flask的引用（启动Flask简易服务器），默认会开启50000的端口提供测试访问
    #  debug=True 以调试的方式启动服务 如果你修改代码 会自动重启 如果代码错误 会把错误 直接报错到浏览器上 和python 中的调试是调试代码 这个是调试逻辑
