# -*- coding:utf-8 -*-
class Human():
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print(self.name, self.age)


s1 = Human("Tarena", 15)
s1.show_info()
s1.Age = 16  # 变量名是区分大小写的 通过slots限定 运行的时候 就报错
s1.age = 16
s1.show_info()
