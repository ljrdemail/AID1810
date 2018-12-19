a=10000

def fx():
    b=20000
    print(b) #可以访问函数内的局部变量
    print(a) #可以方位外部的全局变量
    
print(a)
#print(b)#m没有跑fx 不会打印
fx()
#print(b) #b 外层访问不了函数的局部变量 需要返回