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

    score = property(get_score, set_score) #通过这种方式设定score为属性 外面还是可以用score 而不必用get_score set_score


s = Student("lijiarui", "99", 27)
v = s.score
print(v)

s.score = 999999
print(s.score)
