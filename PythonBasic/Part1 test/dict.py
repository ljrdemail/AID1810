# -*- coding:utf-8 -*-
l=list()
while True:
    str=input("请输入单词和解释以，分隔：")
    d={}
    if(str==""):
        break

    d["Word"]=str.split(",")[0]
    d["exp"] = str.split(",")[1]

    l.append(d)

str=input("请输入你要查询的单词：")
for i in l:
    if(i["Word"]==str):
        print("解释为",i["exp"])
        break