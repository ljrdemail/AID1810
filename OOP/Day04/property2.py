# -*- coding:utf-8 -*-
class Student:
    def __init__(self, name, score, age):
        self.__score = score
        self.__name = name
        self.__age = age

    def get_score(self):
        # 作为getter 用来提供值
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("成绩超出范围！")


s = Student("lijiarui", "99", 27)
v = s.get_score()
print(v)

s.set_score(99999)
print(s.get_score())#m没有改变