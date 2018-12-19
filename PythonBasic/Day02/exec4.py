#判断 正数  负数 0
x=input("请输入需要判断的数:")

xnum=int(x)

if(xnum>0):
    print("正数")
elif(xnum<0):
    print("负数")
else:
    print("是0")