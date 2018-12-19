import mymod

'''
此模块将作为主模块来导入mymod模块
用mymod里的函数和数据 组成我的程序



'''
mymod.fac(6) #在导入的时候 载入  变量 和方法 被加载 （都视为全局变量 即是是方法 也是一个全局变量 ）

mymod.sum(100)

print(mymod.name1)
print(mymod.sum(100))


from mymod import *
fac(10)
print(name2)
