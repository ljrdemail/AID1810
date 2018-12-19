l=list()
for i in range(1,5):
  for j in range(1,5):
      for k in range(1,5):
          s=str(j)+str(j)+str(k)
          l.append(s)


print(l)
print(len(l))