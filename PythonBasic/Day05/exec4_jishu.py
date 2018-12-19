for i in range(1,101):
     if(i%2==1):
         print(i,end=" ")
print()
print("--------------------------------")


# for x in range(0, 100):
#     if x % 2 == 0:
#         continue
#     print(x, end=' ')
# print()


sum=0
for j  in range (1,101):
    if(j%2==0):
        continue
    if (j % 3 == 0):
        continue
    if (j % 5 == 0):
        continue
    if (j % 7 == 0):
        continue
    else:
        sum+=j
   # print(j)
print("不能被2,3,5,7整除的数的和为:",sum)