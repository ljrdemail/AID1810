# 处理与博客相关的路由和视图
from flask import render_template
from . import main


@main.route('/')
def main_index():
    return render_template("index.html")
