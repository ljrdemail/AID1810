from flask import Flask, request, render_template

app = Flask(__name__)


# 测试getlist方法
@app.route("/01-form", methods=['GET', 'POST'])
def form_view():
    method = request.method
    if method == "GET":
        return render_template("Day03_01-form.html")
    elif method == "POST":
        uname = request.form.get("uname")
        hobby = request.form.getlist("hobby")
        country = request.form.getlist("country")
        print(uname, hobby, country)
        return "接收数据成功"


if __name__ == "__main__":
    app.run(debug=True)
