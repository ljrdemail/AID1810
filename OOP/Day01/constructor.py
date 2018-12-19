# -*- coding:utf-8 -*-
class Dog:  # 类名首字母大写 用驼峰命名法
    pass


dog1 = Dog()  # 创建第一个实例对象
print(id(dog1))

dog2 = Dog()  # 创建第二个实例对象
print(id(dog2))

l = list() #创建 一个list 对象
print(id(l))

l2 = list() #创建 一个list 对象 实质跟Dog() 一样 只不过是类不同
print(id(l2))
