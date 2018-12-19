l=int(input("请输入矩形的长度："))

for i in range(0,l):
    for j in range(i+1,i+1+l):
        print(j,end="\t")
    print()