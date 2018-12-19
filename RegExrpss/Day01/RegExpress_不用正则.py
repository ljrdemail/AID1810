s = "70559506@qq.com peter@126.com 12345678@qq.com"
l2 = []
l = s.split(" ")
for i in l:
    if i.count("qq.com") != 0:
        l2.append(i)

print(l2)
