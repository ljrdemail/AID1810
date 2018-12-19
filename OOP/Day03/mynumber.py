# 在自定义的类内添加__str__ 方法和__repr__ 方法 让自定义的类能用str(x) 和repr(x) 的函数返回自定义的字符串
# -*- coding:utf-8 -*-
class MyNumber:
    # 此类用于定义一个自定义的数值类，此类的对象的data属性用于绑定内部数据
    def __init__(self, value):
        self.data = value

    def __str__(self):
        print("__str__方法被调用")
        return "自定义数字：" + str(self.data)

    def __repr__(self):
        print("__repr__方法被调用")
        #return  "MyNumber(%d)"  % self.data
        return repr(self.data)


n1 = MyNumber(100)
n2 = MyNumber(200)
print(repr(n1))
print("可以通过eval转回来",eval(repr(n1)))
print(str(n1))
