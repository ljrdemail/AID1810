# -*- coding:utf-8 -*-
class Dog:
    def eat(self, food):
        print(self.color, '的', self.kinds, '正在吃', food)  # 不像java属性 必须要在定义 类的时候定义 可以在new的时候动态定义属性
        self.last_food=food #为正在吃的狗创建一个属性 用来记住上次吃了什么
    def info(self):
        print(self.color,'的',self.kinds,'上次吃的是',self.last_food)


dog1 = Dog()

dog1.kinds = "导盲犬"  # 为dog1绑定的对象添加kinds属性
dog1.color = "灰色"  # 初次赋值是创建变量color 并半绑定为"灰色"
dog1.color = "黑色"  # 再次赋值则改变color的绑定关系
dog1.eat("骨头")
dog1.info()
print(dog1.color, dog1.kinds)

dog2 = Dog()
dog2.kinds = "哈士奇"
dog2.color = "黑白"
dog2.eat("狗粮")  # 报错 确实要color


