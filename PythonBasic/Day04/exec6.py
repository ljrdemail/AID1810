begin = int(input("请输入开始:"))
end = int(input("请输入结束:"))

# while(begin<end):
#     print(begin,end=" ")
#     begin+=1
count = 1
while (begin < end):
    print(begin, end="\t")
    begin += 1
    if (count % 5 == 0):
        print()
    count +=1

