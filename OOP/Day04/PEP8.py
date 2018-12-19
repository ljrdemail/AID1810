# -*- coding:utf-8 -*-
class Student:

    def __init__(self, name, score, age):
        self.__score = score
        self.__name = name
        self.__age = age

    @property
    def score(self):
        # 作为getter 用来提供值

        return self.__score

    @score.setter
    def score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            print("成绩超出范围！")


s = Student("lijiarui", "99", 27)
v = s.score
print(v)

s.score = 88
print(s.score)
