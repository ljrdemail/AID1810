# -*- coding:utf-8 -*-
class MyList:
    # 自定义的容器类 内部使用内建的列表保存数据
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __len__(self):
        # 此方法为len 调用 此方法的返回值必须为整数 不能为其他的数
        return len(self.data)
        # return len(self) #不能这样 写 要不然递归调用 因为你就是在定义对象的len方法 自己调用自己

    def __repr__(self):
        return "MyList(%s)" % self.data


L = []
L.append({1, 2, 3})
L.append(("A", "B", "c"))
L.append(MyList([4, 5, 6]))  # 为了根内建对象 一样操作

s = 0
for x in L:
    print(x)
    s += len(x) #如果没有定义 name就不能跟内置的一起操作

print(s)
