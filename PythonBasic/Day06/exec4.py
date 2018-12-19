l = list()

while True:
    str = input("请输入字符:")

    if (str == ""): #或者if not str 因为 =""为False not 空 =True 则break
        print("欢迎再次光临")
        break
    l.append(str)

for i in l:
    print(i)

print("你一共输入了%d行文字" % len(l))

sum = 0
for i in l:
    sum += len(i)

print("你输入%d个字符" % sum)
