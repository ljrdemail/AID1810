import time


def liveday():
    dob = input("请输入你出生年月日，以-分隔：")

    year = int((dob.split("-")[0]))
    month = int(dob.split("-")[1])
    day = int(dob.split("-")[2])

    timetuple = (year, month, day, 0, 0, 0, 0, 0, 0)
    birth = time.mktime(timetuple)
    today = time.time()
    gap = today - birth

    tilltoday = gap / 24 / 3600
    print("你活了%d天" % tilltoday)


    w={0:"星期一",1:"星期二",2:"星期三",3:"星期四",4:"星期五",5:"星期六",6:"星期日"}
    # print("你活了",(d2-d1).days,"天")
    print("你出生那天是:",w[timetuple[6]])
    # print("你出生那天是:",w[d1.weekday()])


liveday()
