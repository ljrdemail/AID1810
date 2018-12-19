# -*- coding:utf-8 -*-
class Human:
    total_count = 0  # 类变量 用来记录此类的实例的个数


xiaoli = Human()
print(xiaoli.total_count)  # 类的变量可以通过类的实例直接访问（取值）

xiaoli.total_count = 100  # 可以修改实例的对应的类变量的值 因为自己创建了一份 后访问自己的那一份
print(xiaoli.total_count)

print(Human.total_count)  # 但是修改不了类的类变量的值
