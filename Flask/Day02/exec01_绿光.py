from flask import Flask
from flask import render_template

app = Flask(__name__)


# localhost:5000/01-var
# 目的：实现变量在模板中的显示效果
@app.route('/01_var')
def var_view():
    # 在这个视图处理函数中渲染到01-war.html模板上
    # 渲染的参数1 :name 值为wangwc
    # 渲染的参数2: age  值为37
    return render_template("Day2 01-var.html", name="李嘉睿", age=37, gender="男", songname="绿光", zuoci="王宝强", zuoqu="羽凡",
                           yanchang="贾乃亮")


if __name__ == "__main__":
    app.run(debug=True)
