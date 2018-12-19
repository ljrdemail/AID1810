# -*- coding:utf-8 -*-
class Dog:
    pass


dog1 = Dog()
dog2 = list()
print(isinstance(dog1, Dog))
print(isinstance(dog2, Dog))  # 判断是不是狗的一个实例

print(isinstance("ABC", str))

print(isinstance(123, str))
print(isinstance(123, int))

print(isinstance(3.14,int))
print(isinstance(3.14,float))
