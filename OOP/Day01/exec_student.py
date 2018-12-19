# -*- coding:utf-8 -*-
class Student:
    def __init__(self, name, age, score=0):
        self.name = name
        self.age = age
        self.score = score

    def set_score(self, score):
        self.score = score

    def show_info(self):
        print(self.name, "今年", self.age, "岁 ", "成绩为：", self.score)


L = list()

L.append(Student("小张", 20, 100))
L.append(Student("小李", 18, 98))
L.append(Student("小菜", 19))

L[-1].set_score(70)

for s in L:
    s.show_info()
