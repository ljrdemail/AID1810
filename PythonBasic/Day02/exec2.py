hour=input("请输入小时：")
minute=input("请输入分钟：")
second=input("请输入秒：")

till=int(hour)*3600+int(minute)*60+int(second)

print("你输入的时间距离凌晨00:00:00 过去了%d秒" %till)