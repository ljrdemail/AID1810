def isoushu(x):
    if (x % 2 == 0): #注意一定是返回True或FALSE
        return True
    return False


l = list()
for x in filter(isoushu, range(1, 21)):
    l.append(x)

print("1~20偶数为:", l)


for x in filter(lambda  x:x%2==0,range(1, 21)):
    print(x)