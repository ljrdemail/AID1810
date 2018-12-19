# -*- coding:utf-8 -*-
class Student:
    def __init__(self, name, score, age):
        self.score = score
        self.name = name
        self.age = age


s = Student("lijiarui", "99", 27)
v = s.score #取值
print(v)
s.score = 999999999 #赋值
print(s.score) #被破坏了
