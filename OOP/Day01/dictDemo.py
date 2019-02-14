# -*- coding:utf-8 -*-
class Dog:
    pass


dog1 = Dog()
print(dog1.__dict__)  # {}

dog1.color = "白色"
print(dog1.__dict__)  # {‘color’:’白色’}
dog1.kinds = "比熊"
dog1.age = 2
dog1.name = "果果"
print(dog1.__dict__)
print(dog1.color)
print(dog1.kinds)
print(dog1.__dict__["color"])
del dog1.__dict__['kinds']
# print(dog1.__dict__["kinds"])
# dict就是用来存放实例变量的字典
