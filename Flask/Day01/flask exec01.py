# 练习带参数的route
from flask import Flask

app = Flask(__name__)


@app.route("/calc/<int:num1>/<int:num2>")
def calc(num1, num2):
    # num1 = int(num1)
    # num2 = int(num2)
    s = "<h1>%d+%d=%d</h1>" % (num1, num2, num1 + num2)
    s += "<h1>%d-%d=%d</h1>" % (num1, num2, num1 - num2)
    s += "<h1>%d*%d=%d</h1>" % (num1, num2, num1 * num2)
    s += "<h1>%d/%d=%.2f</h1>" % (num1, num2, num1 / num2)
    s += "<h1>%d%%%d=%d</h1>" % (num1, num2, num1 % num2)
    # 输出% 需要在前面加一个% 转义
    return s


if __name__ == "__main__":
    app.run(debug=True)
