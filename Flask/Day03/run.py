from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/01-parent")
def parent():
    return render_template('Day01_01-parent.html')


@app.route("/02-child")
def child():
    return render_template('Day01_02-child.html')


if __name__ == "__main__":
    app.run(debug=True)
