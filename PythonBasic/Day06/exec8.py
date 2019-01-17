lj=list()
lo=list()
la=list()
while True:
    num=int(input("请输入整数:"))
    if (num==0):
        break
    la.append(num)

lj=[x for x in la if x >0]
print(lj)
lo=[x for x in la if x <0]
print(lo)