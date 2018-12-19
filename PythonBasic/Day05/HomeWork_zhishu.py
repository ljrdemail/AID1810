zhishu = int(input("请输入需要判断是否是质数的数："))

if (zhishu < 2):
    print("不是质数")

else:
    flag = True

    for j in range(2, zhishu):

        if (zhishu % j == 0):
            flag = False
            break

    if (flag):
        print("是素数")
    else:
        print("不是素数")
