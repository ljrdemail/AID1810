x = 100
y = 200
s = "x+y"
v2 = eval(s)  # 此处使用当前作用域的变量作为运行环境
print("v2=", v2)

global_dict = {'x': 10, 'y': 20}
v3 = eval(s, global_dict)#只有全局的 就取全局的
print('v3=', v3)

local_dict = {'x': 1, 'y': 2}
v4 = eval(s, global_dict, local_dict)
print('v4=', v4)  # 又有全局又有局部 优先局部

v5 = eval(s, None, local_dict)
print("v5=", v5) #只有local就取local

v6 = eval(s, None, None)
print("v6=", v6)#如果都没有 则取当前环境的

v7=eval(s,global_dict,{'x':1})
print("v7=", v7)  #21 在global里面找到 y =20 在局部里面找 x 1 =21 优先用局部 局部找不到找global 如果都没有 300 走默认
