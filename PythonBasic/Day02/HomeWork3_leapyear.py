leapyear = int(input("请输入年份："))

flag = (leapyear % 4 == 0 and leapyear % 100 != 0) or leapyear % 400 == 0

print(leapyear, "是闰年") if flag else print(leapyear, "不是闰年")
