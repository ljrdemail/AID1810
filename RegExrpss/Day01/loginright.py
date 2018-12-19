# -*- coding:utf-8 -*-
import re

with open("passwd", "r") as fr:
    l = []
    while True:

        line = fr.readline()

        if re.findall("/sbin/nologin$", line):
            l.append(line)

        if not line:
            break
    print(l)
    print("不能登录的用户一共有：%d个" %len(l))
