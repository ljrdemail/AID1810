# shuix=int(input("请输入三位数"))
#
# b=shuix//100
# s=shuix//10-b*10
# g=shuix%10
#
# print(b)
# print(s)
# print(g)

for i in range(100,1000):
    b=i//100
    s=i//10-b*10
    g=i%10

    shuixianhua=b**3+s**3+g**3
    if(i==shuixianhua):
        print(i,end="\t")


