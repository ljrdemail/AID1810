s = '''

x=10000
y=20000
z=x+y
print(x,"+",y,"=",z)
'''

global_dict={}
exec(s,global_dict)
print("global_dict=",global_dict)
#把结果存入到global_dict 里面 x y z 不存在默认的外部环境
#print(global_dict['x'])
for key in global_dict:
    print(key)
#exec(s) #如果注释掉 下面报错

#print(x, y, z) #里面创建 外面也有 在当前作用域内创建变量 你就当 代码直接写在外面就好
