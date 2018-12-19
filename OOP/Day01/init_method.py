# -*- coding:utf-8 -*-
# 此示例示意初始化方法来为Car类创建实例变量（属性）
class Car:
    '''此类用于描述小汽车的行为'''

    def __init__(self, color, brand, model):
        self.color = color
        self.brand = brand
        self.model = model
        return None #初始化函数没有返回 要返回只能返回None 等同于不写
        #return "" 报错只能返回None或者不反悔
        print("初始化被调用")

    def run(self, speed):
        print(self.color, '的', self.brand, self.model, "正在以", speed, "公里/小时的速度行驶")


# a4=Car()
# a4.run(199)
#Car('蓝色', '吉利', '博瑞GE PHEV 耀领版')  # 有了有参的初始化 方法 就必须传入 初始化值 不能无惨
a4=Car('蓝色', '吉利', '博瑞GE PHEV 耀领版')  # 有了有参的初始化 方法 就必须传入 初始化值 不能无惨
#初始化中的self 指向新生成的car 对象 初始化完成之后 赋值给a4
a4.run(120)

