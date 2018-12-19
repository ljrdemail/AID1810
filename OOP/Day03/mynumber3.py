# -*- coding:utf-8 -*-
class MyNumber:
    def __init__(self, value):
        self.data = value

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)  # 此方法必须返回浮点型数或整形数 不能是str

    def __repr__(self):
        return repr(self.data)

    def __str__(self):
        return str(self.data)


n1 = MyNumber("100")
i = int(n1)
f = float(n1)
print(n1)
print(i)
print(f)

c = complex(n1)
print(c)  # float作为实部 0j作为虚部
b = bool(n1)
print(b)
