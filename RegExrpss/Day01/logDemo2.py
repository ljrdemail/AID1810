# -*- coding:utf-8 -*-
import re

with open("tedu.log", "r")as fr:
    lines = fr.readlines()
    for line in lines:
        ip = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line)
        print(ip)
