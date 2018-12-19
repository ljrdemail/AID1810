# -*- coding:utf-8 -*-
# 此示例示意将自定义的类A 创始的对象作为环境管理器
# 让A对象能使用with语句进行管理

class A:
    def __enter__(self):
        print("已经进入with语句")
        print("enter里面的地址",self)
        return self  # 此self对象将用as 变量进行绑定

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("已经离开with 语句")
        print("exc_type=", exc_type)  # exc_type绑定异常类型 如果with语句中没有异常 三个都是None
        print("exc_val=", exc_val)  # 绑定错误对象（信息） 如果with语句中没有异常 三个都是None
        print("exc_tb=", exc_tb)  # 绑定 taceback（追踪） 信息 堆栈调用关系 如果with语句中没有异常 三个都是None
        if(exc_type!=None):
            print("在这里关文件 或释放资源")

    def __del__(self):
        print(self,"被销毁")


with A() as a:  # 等同于 a=A()
    print("这是with 语句内部的一条语句")
    5/0
    print("返回的跟enter里面的id一样",a)
    int(input("请输入数字:"))

print("程序结束")  # 如果报错跑不到这里 更加说明with处理不了异常 只能关文件 等释放资源的活
