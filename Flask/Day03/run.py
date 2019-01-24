from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/01-parent")
def parent():
    return render_template('Day03_01-parent.html')


@app.route("/02-child")
def child():
    return render_template('Day03_02-child.html')


# localhost:5000/03-request
# 目的:查看request中的成员
@app.route('/03-request')
def request_views():
    # print(dir(request))
    # 获取请求中的各个参数
    scheme = request.scheme  # 协议
    method = request.method  # 请求方式
    args = request.args  # get请求数据
    form = request.form  # POST请求数据
    cookies = request.cookies  # 获取cookies
    files = request.files  # 获取上传文件
    path = request.path  # 请求资源的路径
    full_path = request.full_path  # 请求资源路径
    url = request.url  # 完整路径

    header = request.headers  # 请求消息头
    # refer =request.headers["Referer"]
    # if "Referer" in request.headers:
    #     refer = request.headers['Referer'] #避免如果不是转过来没有referer 导致报错或
    referer = request.headers.get('Referer', "/")  # 如果有则源地址 没有则返回/ 就是首页
    return render_template("Day03_03-request.html", params=locals())


# localhost:5000/04-referer
# 目的:在03-request中查询请求源地址 - Referer
# 如果直接访问/03-request 没有referer 如果通过访问/04-referer 再跳转到03 就有referer
@app.route('/04-referer')
def referer_views():
    return "<a href=/03-request>去往03-request</a>"


# localhost:5000/05-get
# 目的:接收get请求提交的数据
@app.route('/05-get')
def get_views():
    # 模拟访问路径localhost:5000/05-get?name=xxx&age=xxx 以字典的方式获取
    name = request.args['name']
    age = request.args['age']
    return "<h1>提交的数据name:%s,age:%s</h1>" % (name, age)


# localhost:5000/06-post
# 目的:接收post请求的数据
# 判断用户的请求方式
# 如果是get请求的话,则渲染06-post.html模板
# 如果是post请求的话,则可以接收请求提交的数据
# 需要在路由中指明允许接收的请求方法都有什么
@app.route('/06-post', methods=["POST", "GET"])
def post_views():
    # 判断请求方式是get还是post
    method = request.method
    if method == "GET":
        return render_template("Day03_06-post.html")
    elif method == "POST":
        # 接收POST请求所提交的数据
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        return "<h1>uname:%s,upwd:%s</h1>" % (uname, upwd)


# localhost:5000/
# 目的:定义首页访问路径 用于验证如果 referer = request.headers.get('Referer', "/") 会跳转到这一页
@app.route('/')
def index():
    return "<h1>这是我的首页内容</h1>"


if __name__ == "__main__":
    app.run(debug=True)
