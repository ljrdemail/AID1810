import math as m

import math

r = float(input("请输入圆的半径："))

print("面积为:", m.pi * r ** 2)

a = float(input("请输入圆的面积："))
print("圆的半径为:", m.sqrt(a / m.pi))
