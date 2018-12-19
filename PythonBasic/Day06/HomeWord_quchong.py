import random

l = list()

for i in range(1, 101):
    l.append(random.randint(1, 100))

print("原数组为：",l)

l2 = list()
l3 = list()


for i in l:
    if (i not in l2):
        l2.append(i)

print("去重后",l2)

for j in l:
    if(j not in l3 and l.count(j)==2):
        l3.append(j)

print("l3为：",l3)

