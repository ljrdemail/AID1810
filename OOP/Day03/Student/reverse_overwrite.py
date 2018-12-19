# -*- coding:utf-8 -*-
class MyList:
     #自定义的容器类 内部使用内建的列表保存数据
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __reversed__(self):
          #此方法为len 调用 此方法的返回值必须为整数 不能为其他的数
         return MyList(reversed(self.data))
         #return len(self) #不能这样 写 要不然递归调用 因为你就是在定义对象的len方法 自己调用自己
    def __repr__(self):
        return  "MyList(%s)" %self.data



myl=MyList([1,-2,3,-4]) #从列表转为字符串 %s
myl2=reversed(myl)
print(myl)
print(myl2) #object 没有len 所以要自己写 否则出错



