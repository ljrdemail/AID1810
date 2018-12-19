# -*- coding:utf-8 -*-
with open("tedu.log", "r")as fr:
    lines = fr.readlines()
    for line in lines:
        ip = line[0:13]
        print(ip)
