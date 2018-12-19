l=list()
for i in range(40):
    if(i==0 or i==1):
        l.append(1)
    else:
        l.append(int(l[i-2])+int(l[i-1]))


print("前40个斐波那契数列为：",l)