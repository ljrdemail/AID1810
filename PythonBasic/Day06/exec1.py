l = list()
for i in range(1, 4):
    num = int(input("请输入正第%d个整数:" % i))
    l += [num]

print(l)
print("最大值为:%d" % max(l))
print("最小值为:%d:" % min(l))
print("平均值为:%.2f" % (sum(l) / len(l)))
