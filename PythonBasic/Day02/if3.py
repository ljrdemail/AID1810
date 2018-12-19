# 输入并判断基数还是偶数

x = input("请输入需要判断的数：")

xnum = int(x)

if (xnum % 2):
    print("是奇数")
else :
#else: #else 子句当上述所有所有的条件都不符合的时候走else
    print("是偶数")

