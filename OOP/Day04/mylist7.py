# -*- coding:utf-8 -*-
class MyList:

    def __init__(self, iterable=()):
        self.data = [x for x in iterable]

    def __repr__(self):
        # return "MyList(%s)" % self.data
        return repr(self.data)

    def __getitem__(self, item):
        if type(item) is int:
            print("用户在做索引操作")
        elif type(item) is slice:
            print("用户在做切片操作")
            print("起始值为", item.start)
            print("终止值为", item.stop)
            print("步长值为", item.step)

        print("getitem被调用 item=", item)
        return self.data[item]

    def __setitem__(self, key, value):
        print("setitem被调用 key=%r value=%r" % (key, value))
        self.data[key] = value
        return self.data

    def __delitem__(self, key):
        print("delitem被调用 key=%r " % (key))
        return self.data.pop(key)


L1 = MyList([1, -2, 3, -4, 5])
# lst=L1[::2] #切片调用的是 getitem
# print(lst)
lst = L1[0:10:2]
print(lst)
L1[0:2] = [5, 6]
print(L1)
del [L1[0]]
print(L1)
