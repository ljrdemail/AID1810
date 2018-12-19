long = int(input("请输入三角形宽度："))

i = 1
while (i <= long):
    print("*" * i)
    i += 1

    print("")

print("-----------华丽丽的分割线-------------")
i = 1
while (i <= long):
    print((long - i) * " " + "*"* i)
    i += 1
    print()


print("-----------华丽丽的分割线-------------")
i = 0
while (i < long):
    print(i * " " + "*"* (long-i))
    i += 1
    print()


print("-----------华丽丽的分割线-------------")
i = 0
while (i < long):
    print("*"* (long-i))
    i += 1
    print()

