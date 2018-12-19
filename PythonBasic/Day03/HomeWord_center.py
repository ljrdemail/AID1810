str1=input("请输入第一句：")
lenstr1=int(len(str1))
str2=input("请输入第二句：")
lenstr2=int(len(str2))
str3=input("请输入第二句：")
lenstr3=int(len(str3))

# max=lenstr1;
# if(lenstr2>max):
#     max=lenstr2
#
# if(lenstr3>max):
#     max=lenstr3

max_length=max(lenstr1,lenstr2,lenstr3)

print("+",(max_length)*"-","+")
print("|",str1.center(max_length),"|")
print("|",str2.center(max_length),"|")
print("|",str3.center(max_length),"|")
print("+",(max_length)*"-","+")