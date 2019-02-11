from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello World"


@app.route("/01-server")
def server01():
    return "这是我的第一个AJAX请求"


if __name__ == "__main__":
    app.run(debug=True)
