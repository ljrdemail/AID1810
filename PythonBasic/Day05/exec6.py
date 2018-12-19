l = list()
sum = 0
while True:
    i = int(input("请输入正整数："))
    if (i < 0):
        break
    l += [i] #必须放可迭代对象 不能放一个单独的对象 所以不能list(n)

    #l.append(i)
    sum += i

print("列表为",l)
print("和为：",sum)

sum2 = 0
for j in l:
    sum2 += j ** 2

print("平方和为:",sum2)
