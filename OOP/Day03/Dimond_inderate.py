# -*- coding:utf-8 -*-
class A:
    def go(self):
        print('A')
        # super(A, self).go()#报错object里面没有go 方法


class B(A):
    # pass
    def go(self):
        print('B')
        super(B, self).go()  # super不是按照继承关系来的 是按照MRO来的 所以是C 不是A 虽然B不是继承于C super是在调用mro 中在先的


class C(A):
    # pass
    def go(self):
        print('C')
        super(C, self).go()  # A


class D(B, C):
    # pass
    def go(self):
        print('D')
        super(D, self).go()  # 调用谁？ B
        # 如果直接向要掉A
        # A.go(self) #尽量不要这样 怕递归调用
        super(C, self).go()  # 调用A类的go方法


d = D()  # D- B -C -A
d.go()

print("打印D类的MRO")
for cls in D.__mro__:
    print(cls)
