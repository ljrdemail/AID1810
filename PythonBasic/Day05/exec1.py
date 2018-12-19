str=input("请输入字符串：")
count=0
# for i in str:
# #     if(i==" "):
# #         count+=1
# #
# # print("这个字符一共有%d个空格"% count)

for  i in str:
    if(0<=ord(i)<=127):
        count+=1

print("这个字符一共有%d个英文字符:" %count)

