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
    return render_template("Day2 01-var.html", name="李嘉睿", age=37)


@app.route('/02-var')
# 目的：验证允许放在模板中作为变量的数据类型
def var02():
    # 字符串
    name = "wangwc"
    # 数字
    age = 37
    # 元素 ，列表 字段
    tup = ('抽烟', '喝酒', '保健')
    list = ['赵丽颖', '赵蒙蒙', '葛老师']
    dict = {"WFR": "夫人：王夫人", 'LXG': "儿子:李小超", 'LEG': "邻居：李二狗"}
    p = person()
    p.name = "王伟超老师"
    return render_template("Day 02_02-var.html", name=name, age=age, tup=tup, list=list, dict=dict, person=p)


class person(object):
    name = None;

    def say(self):
        return "hello,my name is %s" % self.name


if __name__ == "__main__":
    app.run(debug=True)
