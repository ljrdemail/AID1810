# -*- coding:utf-8 -*-

class A:
    def m(self):
        print("A.m被调用！")


class B:
    def m(self):
        print("B.m被调用！")




class AB(A, B):
    pass


ab1 = AB()
ab1.m()  # 调用谁不确定  class AB(A, B):  中谁在前先调用谁 class AB(A, B) 调用A class AB(B, A) 调用B  放在前面的 MOR 在先 实际上还是取决于 MOR

