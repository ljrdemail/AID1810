#输入一个月份 判断这个月是哪个季度


x = input("请输入需要查询的月份：")

xnum = int(x)

if(1<=xnum<=12):
    print("合法月份")
    if (1 <= xnum <= 3):
        print("第一季度")
    elif (4 <= xnum <= 6):
        print("第二季度")
    elif (7 <= xnum <= 9):
        print("第三季度")
    elif (10 <= xnum <= 12):
        print("第四季度")

else:
    print("输入有误")

