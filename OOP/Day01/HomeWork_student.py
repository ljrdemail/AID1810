# -*- coding:utf-8 -*-
l = list()


class Student:

    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def add_student(self):

        d = {}
        global l
        d.update({"name": self.name, "age": self.age, "score": self.score})
        l.append(d)

    def del_student(self):
        global l
        for i in l:
            if i["name"] == self.name:
                l.remove(i)

    # def get_count(self):
    #
    #     return len(l)

    def get_avg_score(self):
        sum = 0
        global l
        for i in l:
            sum += i["score"]

        return sum / len(l)

    def get_avg_age(self):
        sum = 0

        for i in l:
            sum += i["age"]

        return sum / len(l)


stu1 = Student("李嘉睿", 20, 99)
stu1.add_student()
stu2 = Student("潘仁晓", 21, 98)
stu2.add_student()
stu3 = Student("潘华", 22, 97)
stu3.add_student()
print("学生个数",len(l))
print("平均分为：",stu3.get_avg_score())
print("平均年龄Wie：",stu3.get_avg_age())
# stu3.del_student()


