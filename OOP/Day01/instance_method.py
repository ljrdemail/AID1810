# -*- coding:utf-8 -*-
# 此示例示意实例方法的定义和调用
class Dog:
    '''这是一种小动物的定义'''

    def eat(self, food):
        '''此方法用来描述小狗的吃的行为'''
        print("小狗正在吃%s" %food)
        print("里面的id为：",id(self),"正在吃",food) #id和外面的一样 就是self带进来的

    def sleep(self,hour):
        print("id为:",id(self),'的小狗睡了',hour,"小时")


# dog1=Dog()
# dog1.eat("骨头")
#
# dog1.sleep(1)
#print("dog1的id为",id(dog1))

# dog2=Dog()
#
# dog2.eat("狗粮")
# dog2.sleep(3)
#print("dog2的id为",id(dog2))
#Dog.eat(dog1,"包子") #等同于 dog1.eat("包子")