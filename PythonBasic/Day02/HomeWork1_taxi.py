mile=float(input("请输入公里数："))
amount=0.0
if(mile <=3):
    print("您的车费为13元" )
elif(3<mile<=15):
    amount=13+(mile-3)*2.3
    ramount=round(amount,2)
    print("您的车费为%.2f"  %ramount)
else:
    amount = 13 + (mile - 15) * 3.45+12* 2.3
    ramount = round(amount, 2)
    print("您的车费为%.2f" % ramount)