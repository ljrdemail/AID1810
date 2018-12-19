import datetime
import time

hour = int(input("请输入小时！24小时制:"))
minute = int(input("请输入分钟！24小时制:"))

hn = int(datetime.datetime.now().strftime("%H"))
hm = int(datetime.datetime.now().strftime("%M"))

if (hour < hn):
    print("不能设定比当前时间早的时间")

if (hour == hn and (minute < hm)):
    print("不能设定比当前时间早的时间")

hc = (hour - hn) * 3600
mc = (minute - hm) * 60

cj = hc + mc

while True:
    if (cj == 0):
        print("时间到")
        break
    time.sleep(1)
    cj -= 1
    