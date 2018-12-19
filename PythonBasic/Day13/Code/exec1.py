import random


def guessgame(corrnum):
    print("作弊：", corrnum)
    count = 0
    while True:
        ui = int(input("猜吧!"))
        if (ui > corrnum):
            print("大了!")
            count += 1
            continue
        if (ui < corrnum):
            print("小了!")
            count += 1
            continue
        if (ui == corrnum):
            print("恭喜你答对了!")
            count += 1
            break
    return count



x = random.randint(0,100)
c = guessgame(x)
print("经过了%d次猜对" % c)

#最快的查找是一半一半的猜 就是二分法查找 log(101,2)