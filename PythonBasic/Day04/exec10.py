long = int(input("请输入长度："))

print("#" * long)
i = 1
while (i < long - 1):
    print("#", " " * (long - 2), "#", sep="")
    i += 1
if (long > 1):
    print("#" * long)

