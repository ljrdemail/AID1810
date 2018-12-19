# -*- coding:utf-8 -*-
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def speek(self, language):
        print("i can speak%s" % language)



class chinese(Human):

    def get_hometome(self, logcation):
        print("我家乡是:%s" % logcation)


print(issubclass(chinese, (Human,str)))
print(issubclass(chinese, (str)))