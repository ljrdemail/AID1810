str = input("请输入一段字符:")

L = list(str)

l2 = list()
for i in L:
    if (i not in l2):
        l2.append(i)

for i in l2:
    print("%s 出现了：%d次" % (i, L.count(i)))
