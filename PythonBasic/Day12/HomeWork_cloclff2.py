import time

while True:
    hour = time.localtime(time.time())[3]
    minute = time.localtime(time.time())[4]
    sec = time.localtime(time.time())[5]

    print("%02d:%02d:%02d" % (hour, minute, sec), end="\r")

    time.sleep(1)
