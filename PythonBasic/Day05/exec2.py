for i in range (1,21):
     print(i,end="\t")

print()
print("-------------------------")

n=int(input("请输入n的值:"))

sum=0
for j in range(1,n+1):
    if(j<n):
      print(j,"+",end=" ")
    if(j==n):
      print(j, "=", end=" ")
    sum+=j

print(sum)