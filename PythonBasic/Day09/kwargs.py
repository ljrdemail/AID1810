def func(**kwargs):
    print("参数个数是:", len(kwargs))
    print("kwargs:", kwargs)

func(a=1,b=2,c=3) #必须通过关键字传参或者关键字典传参进

func()

d1={"name":"小张","age":20,"score":100}
func(**d1) #不能func(d1)提示你在位置传参 要**拆 然后在函数内再打包成字典

