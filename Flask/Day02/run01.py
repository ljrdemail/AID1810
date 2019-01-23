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
    person = Person()
    person.name = "王伟超老师"

    # params = {"name": name, "age": age, "tup": tup, "list": list, "dict": dict, "person": person}

    params = locals()  # 所有局部变量 不用一个个的打了
    print(locals())

    # return render_template("Day 02_02-var.html", name=name, age=age, tup=tup, list=list, dict=dict, person=person)
    # return render_template("Day 02_03-var.html", params=params)
    return render_template("Day 02_03-var.html", params=params)


@app.route('/03-if')
def if_view():
    name = "王老师"
    age = 61
    return render_template("Day02_04_if.html", params=locals())


# 先把模板交给python解释器 解释这些标签 然后再交给浏览器渲染 所以可以动静结合

@app.route("/04-for")
def for_view():
    list = ["李嘉睿", "潘仁晓", "李幼兰", "黄翠英", "潘华", "潘仁娟", "李昮"]
    dict = {"SWK": "孙悟空", "PJL": "潘金莲", "GY": "关羽", "LLL": "刘姥姥"}
    return render_template("Day02_05_for.html", params=locals())


# 熟悉宏的声明和使用
@app.route("/05-marco")
def macro_view():
    list = ["李昮", "潘华", "李幼兰", "黄翠英", "李嘉睿", "潘仁晓", "潘仁娟"]
    return render_template("Day02_06_marco.html", params=locals())



class Person(object):
    name = None;

    def say(self):
        return "hello,my name is %s" % self.name


if __name__ == "__main__":
    app.run(debug=True)
