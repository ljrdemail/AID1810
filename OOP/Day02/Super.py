# -*- coding:utf-8 -*-


class A:
    def work(self):
        print("A.work被调用")


class B(A):
    def work(self):
        print("B.work被调用") #覆盖了父类的同名方法
    def do_work(self):
        self.work()
        super(B,self).work() # self 必须是B的类型或者他的子类 不能随便填 比如你填bool
        super().work()#等同于 super(B,self).work()

b=B() #创建实例
# b.work() #B.work被调用
#
# super(B,b).work() #A.work被调用
b.do_work()

#super.work() super无参只能在方法里面调用 必须super(B,b).work()


