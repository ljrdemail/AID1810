# 练习多url route
from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/index")
@app.route("/<int:pagenum>")
@app.route("/index/<int:pagenum>")
def page(pagenum=1):  #给默认值
    return "你要看的页数是第%d页" % pagenum


if __name__ == "__main__":
    app.run(debug=True)
