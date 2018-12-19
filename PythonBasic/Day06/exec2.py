l = list()
count=0
while True:
    num = int(input("请输入正整数，以-1结束！"))
    if (num == -1):
        break
    if (num != -1):
        l += [num]  # 追加 尾插
        #count+=1

print("你一共输入了%d个数" % len(l))
#print("你一共输入了%d个数" % count) #方法2

if (len(l) == 0):
    print("列表为空没有最大值")
else:
    print("最大值为:%d" % max(l))


# max=0
#
# for i in l:
#     if(i>max):
#         max=i
# print("最大值为:%d" % max)
