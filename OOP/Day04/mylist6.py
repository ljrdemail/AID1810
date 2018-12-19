# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        # return "MyList(%s)" % self.data
        return repr(self.data)

    def __getitem__(self, item):
        print("getitem被调用 item=", item)
        return self.data[item]

    def __setitem__(self, key, value):
        print("setitem被调用 key=%r value=%r" %(key,value))
        self.data[key] = value
        return self.data
    def __delitem__(self, key): # 注意是index 不是内容
        print("delitem被调用 key=%r " % (key))
        return self.data.pop(key)


L1 = MyList([1, -2, 3, -4, 5])
L2 = L1[3]

print(L2)

L1[3] = 2
print(L1)

del L1[3]
print(L1)

