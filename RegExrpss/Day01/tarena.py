# -*- coding:utf-8 -*-
import re

with open("passwd", "r") as fr:
    index = 0;
    while True:

        line = fr.readline()
        index += 1
        if re.findall("^tarena", line):
            print(re.findall("^tarena", line))
            print("在%d行找到了:tarena!" %index)

        if not line:
            break
