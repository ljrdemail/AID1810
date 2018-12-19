# -*- coding:utf-8 -*-
class Dog:
    pass


dog1 = Dog()
dog2 = [1, 2, 3, 4]

print(dog1, dog2)
print(type(dog1),type(dog2))
#或
print(dog1.__class__,dog2.__class__) #  new对象的时候就绑定了 这个对象的类
print(dog1.__class__ is Dog)

dog3=dog1.__class__()#调用构造函数创建一个与dog1 同类的对象
#返回一个新的 dog对象 dog3
print(dog3)

#class 属性就是用来创建此实例的类