sum=0
while True:
    i=int(input("请输入大于0的整数："))
    if (i<0):
        break
    sum+=i

print("你刚刚输入的正整数的和是:%d" %sum)