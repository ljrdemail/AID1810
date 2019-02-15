# 处理与博客相关的路由和视图
from . import main
from flask import render_template
from ..models import *
from .. import db


@main.route('/')
def main_index():
    # 查询Category中所有的分类信息
    categories = Category.query.all()
    topics = Topic.query.all()

    return render_template('index.html', params=locals())
