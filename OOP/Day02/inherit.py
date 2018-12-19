# -*- coding:utf-8 -*-
# 此示例示意单继承的语法

class Human:
    '''
    此类描述人类的共有行为


    '''

    def say(self, what):
        print("说:", what)

    def walk(self, distance):
        print("走了", distance, '公里')


class Student(Human):
    def study(self, content):
        print("学习了", content)


class Teacher(Human):
    def teach(self, teach):
        print("教了:", teach)


s1 = Student()
s1.say("感觉有点累")
s1.walk(4)
s1.study("phthon")

t1 = Teacher()
t1.say("今天晚上吃什么？")
t1.walk(6)
t1.teach("phthon")

h1 = Human()
h1.say("今天天气真好")

h1.walk(5)
