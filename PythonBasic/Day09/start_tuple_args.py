def func(*args):
    print(" 实参个数是：",len(args))
    print("args=",args)

func() #绑定空元组
func(1,2,3,4)#绑定(1,2,3,4)
func(1,2,3,4,"ABCD",None,False)
#args不能接受关键字传参
#func(a=100) #func(*{'a':100})