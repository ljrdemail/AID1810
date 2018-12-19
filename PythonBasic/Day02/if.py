# 输入并判断基数还是偶数

x = input("请输入需要判断的数：")

xnum = int(x)

if (xnum % 2 == 0):
    print("是偶数")
#elif (xnum % 2 == 1):
else: #else 子句当上述所有所有的条件都不符合的时候走else
    print("是奇数")

