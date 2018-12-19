str = input("请输入一段字符:")
d={}
for x in str:
   if x not in d:
       d[x]=1
   else:
       d[x]+=1

for x,count in d.items():
   print(x,":",count,"次")