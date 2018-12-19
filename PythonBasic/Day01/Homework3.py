hourminute=60*60
time=63320

hour=time//hourminute
minute=(time%hourminute)//60
second=(time%hourminute)%60

print("经历了%d小时%d分钟%d秒" %(hour,minute,second))