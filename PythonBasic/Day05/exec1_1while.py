str=input("请输入字符串：")
count=0
i=0
# while (i<int(len(str))):
#     if(str[i]==" "):
#         count+=1
#     i+=1
#
# print("这个字符一共有%d个空格"% count)

while (i<int(len(str))):
    if (0 <= ord(str[i]) <= 127):
        count += 1
    i += 1
print("这个字符一共有%d个英文字符:" %count)