l = list()
while True:
    str = input("请输入：")
    if (str == ''):
        break
    l.append(str)

for no, x in enumerate(l, 1):
    print("第%d行为%s" % (no, x))
