# -*- coding:utf-8 -*-
class MyList:
    # 自定义的容器类 内部使用内建的列表保存数据
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __len__(self):
        # 此方法为len 调用 此方法的返回值必须为整数 不能为其他的数
        print("len方法被调用")
        # 当被bool调用 0 为假 非0 真
        return len(self.data)
        # return len(self) #不能这样 写 要不然递归调用 因为你就是在定义对象的len方法 自己调用自己
        # return 0


    def __repr__(self):
        return "MyList(%s)" % self.data

    # def __bool__(self):
    #     print("布尔方法被调用")
    #     return False


myl = MyList([1, -2, 3, -4])  # 从列表转为字符串 %s
# print(myl)
# print(len(myl))  # object 没有len 所以要自己写 否则出错
print(bool(myl))  # 1 bool 2 len 3 默认为真

if myl:
      print("myl为真")
else:
    print("myl为假")