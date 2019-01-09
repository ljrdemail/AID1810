l=list()
for i in range(2, 101):
    flag=True
    for  j in range(2,i):
       if(i%j==0):
           flag=False
           break

    if(flag):
        l.append(i)

print("质数列表为:",l)