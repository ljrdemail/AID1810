# 用于演示FLASK框架的搭建
from flask import Flask
from flask import url_for
from flask import render_template

# 将当运行的主程序构建成Flask应用，以便接收用户请求（request）并给出响应(response)
app = Flask(__name__)


# @app.route("/") FLASK中的路由定义，主要匹配用户的访问路径 ‘/’表示的是整个网站的根路径
# def index() 表示匹配上访问路径之后路的处理程序 也就是Java中的action 也就是MTV 中的 V MVC的C  视图处理函数必须要有返回值 这个例子中的返回值是字符串 表示要响应给客户端浏览器的内容 也就是spring 里面的mapping
# @app.route('/')  # Flask(__name__)返回值叫啥 @后就叫啥
# def index():  # 不是强制/的必须叫 index 名字随便 是根据route 决定
#     return "This is my First flask demo"


@app.route('/abc')  # 必须要有/
def abc():
    return "This is abc application"


# 声明一个带参数的理由
@app.route("/show/<name>")
def show(name):  # 要和尖括号中的名字一致
    return ("<h1>传递过来的名字是:%s</h1>" % name)


# 声明带两个参数的路由
@app.route('/show/<name>/<int:age>')
def showview(name, age):
    print("name的数据类型为%s" % type(name))
    print("age的数据类型为%s" % type(age))
    # print(int(age))
    return '姓名:%s,年龄：%d' % (name, age)


# 传进来都视为str 你需要当成int 自己赚

# 定义多URL 的路由匹配
# localhost:5000/
# localhost:5000/index
# localhost:5000/default
# 访问以上三个任意一个路径的时候都给出统一的响应
@app.route("/")
@app.route("/index")
@app.route("/default")
def index():
    return "首页都返回这个"


# 测试url地址反向解析
@app.route("/admin/login/form/url/show/<name>")
def admin_show(name):
    return "这是admin下login下的form下的url下的show的访问路径,传递进来的参数为%s" % name


@app.route("/url")
def url():
    # 通过admin_show解析出相应的访问路径
    # 将路径构建成a标记进行相应
    url_show = url_for('admin_show',name="wangwc")
    print('admin_show:%s' % url_show)
    return "<a href='%s'>访问admin_show()</a>" % url_show

@app.route("/temp")
def temp():
    #渲染01-template.html模板文件到客户端浏览器
    html=render_template("01-template.html") #会自动在templates目录里面去找
    print(html)
    return html




if __name__ == "__main__":
    app.run(debug=True)
    # 运行Flask的引用（启动Flask简易服务器），默认会开启50000的端口提供测试访问
    #  debug=True 以调试的方式启动服务 如果你修改代码 会自动重启 如果代码错误 会把错误 直接报错到浏览器上 和python 中的调试是调试代码 这个是调试逻辑
