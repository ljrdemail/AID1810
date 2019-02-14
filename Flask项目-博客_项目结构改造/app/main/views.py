# 处理与博客相关的路由和视图
from . import main
from flask import render_template

@main.route('/')
def main_index():
    return render_template('index.html')
