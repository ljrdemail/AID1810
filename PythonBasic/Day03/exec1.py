line = int(input("请输入矩形的宽度:"))

print("#" * line)
if (line == 1):
    print("#")
    print("#")
    print("#" * line)
else:
    print("#", " " * (line - 2), "#", sep="")  # 把自动空的去掉
    print("#", " " * (line - 2), "#", sep="")  # 把自动空的去掉
    print("#" * line)

