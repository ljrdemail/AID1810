# -*- coding:utf-8 -*-
class MyList:
     #自定义的容器类 内部使用内建的列表保存数据
    def __init__(self,iterable=()):
        self.data=[x for x in iterable]
    def __len__(self):
          #此方法为len 调用 此方法的返回值必须为整数 不能为其他的数
         return len(self.data)
         #return len(self) #不能这样 写 要不然递归调用 因为你就是在定义对象的len方法 自己调用自己
    def __repr__(self):
        return  "MyList(%s)" %self.data

myl=MyList([1,-2,3,-4]) #从列表转为字符串 %s
print(myl)
print(len(myl)) #object 没有len 所以要自己写 否则出错

myl2=MyList()
print(myl2)
print(len(myl2))
