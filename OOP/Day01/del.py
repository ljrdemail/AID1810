# -*- coding:utf-8 -*-
class Dog:
    pass


dog1 = Dog()
dog1.color = "白色"
print(dog1.color)
del dog1.color #注意不是del dog1这样 是删除 dog1 对象 我们要的是删除属性 不是整个对象
# print(dog1.color)
