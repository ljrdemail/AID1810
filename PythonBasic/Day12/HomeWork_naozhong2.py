import time

hour = int(input("请输入小时！24小时制:"))
minute = int(input("请输入分钟！24小时制:"))

while True:

    if (time.localtime(time.time())[3] == hour and time.localtime(time.time())[4] == minute):
        print("时间到")
        break
