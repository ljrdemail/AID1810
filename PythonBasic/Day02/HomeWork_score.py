a = float(input("请输入第一科成绩:"))
b = float(input("请输入第二科成绩:"))
c = float(input("请输入第二科成绩:"))

if (a > b):
    minv = a
    a = b
    b = minv

if (a > c):
    minv = a
    a = c
    c = minv

if (b > c):
    minv = b
    b = c
    c = minv

print("最高分为:",c)
print("最低分为:",a)
avg=round((a+b+c)/3,2)
print("平均分为:",avg)
