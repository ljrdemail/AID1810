# -*- coding:utf-8 -*-
import sys
class Car:
    def __init__(self, info):
        self.info = info
        print("汽车", info, '对象被创建！')

    def __del__(self):
        '''析构方法不能有self以外的参数'''

        print("汽车", self.info, "将被销毁！")
        # self.file.close() 析构方法常用于 比如关文件 收拾残局 作用


c1 = Car("BYD EV450")  # 创建对象
# del c1  # 删除变量 同时解除与对象的绑定关系
L = []
L.append(c1)
print(sys.getrefcount(c1),"个引用")
del c1  # 请问 此时汽车对象有没有别销毁 没有 因为 L里面 还指向对象 引用计数从2 变为1 还有指向 不会销毁
# 因此即使你调用了析构方法 还是没销毁对象 所以python语言建议 不要用析构方法 收拾残局 因为你不知道 还有没有东西指向想要销毁的对象


input("请输入回车键结束程序执行！")  # 如果对象一直没有被销毁 程序结束的时候 也会自动销毁（Python 收回对象和变量的内存空间 一旦对象被收回调用了del）
#  #这一句完了 也会销毁
print("程序结束")
