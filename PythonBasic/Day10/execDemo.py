x = 100
y = 200
s = '''

print("hello")
z=x+y
print(z) #如果你用eval 就不能a=x+y 因为用了赋值表达式


'''

print(exec(s))
print(z) #跑完之后z 也有了 等同于放在代码中直接执行 所以你在里面修改 x y 的话 x y 会受影响
