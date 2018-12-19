local_dict = {}
global_dict={}
inp=''''''
while True:
    str = input("请输入程序：>>>")
    if (str == 'quit()'):
        break
    inp=inp+str+"\n"

#exec(inp, global_dict, local_dict) #优先存到局部变量
#exec(inp, global_dict, None) #如果没有局部变量给你存 那就存到全局变化量

#print(local_dict)
#print(global_dict['x']+global_dict['y'])

exec(inp)#如果两个都不带 存在当前环境中

# print(local_dict)
# print(global_dict)
print(x)
print(y)


