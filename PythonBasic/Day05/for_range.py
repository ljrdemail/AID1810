i=6

for x in range(1,i):
    print("x=",x,'i=',i)
    i-=1
    #i初始值为6 range 只运行一次（1~5） 可迭代对象已经生成 即使后来i 减少 还是 1~5 不会重新生成对象