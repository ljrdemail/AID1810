l = list()

while True:
    num = int(input("请输入正整数:"))
    if (num < 0):
        break
    if (l.count(num) > 0):
        print("请输入不重复的数!")
        continue
    l += [num]


print("这些数的和为:%d" % sum(l))
print("这些数中最大的数为:%d" % max(l))
l2 = l.copy()
l.sort(reverse=True)
print("这些数中第二大的数为:%d" % l[1])

l2.remove(min(l2))

print(l2)
