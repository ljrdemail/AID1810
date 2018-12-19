# -*- coding:utf-8 -*-
class Human:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        print("init方法被调用")

    def infos(self):
        print("姓名:", self.name)
        print("年龄:", self.age)



class Studnet(Human):
    def __init__(self,n,a,s=0): #子类的初始化方法被调用 父类的就不用了
        # self.name = n 父类的东西就应该父类来做
        # self.age = a
        #super(Studnet,self).__init__(n,a) #显示调用父类的初始化方法 让父类做父类该做的
        super().__init__(n, a)  # 方法内调用可以省略
        self.score=s #子类只关注于独有的
        print("student init 被调用")


    def infos(self):
        # print("姓名:", self.name)
        # print("年龄:", self.age)
        super().infos() #让父类干父类该干的事情
        print("成绩:", self.score)


# h1=Human("小张",20)
# h1.infos()

#s1 = Studnet() #如果不传参 因为 调用了父类的有参数初始化方法 提示少传了n a 如果父类没有有参的init 可以不传
#dog1=Dog() 调用了父类的无参初始化方法 （啥也不干）
s1=Studnet("小李",30,98)
s1.infos() #调用父类的 已有方法 因为 父类缺少 score 所以不打印 除非你覆盖