v=100
def f1():

    v=200 #不会影响 全局的100
    global v  # 声明此V为全局的那个V 不是局部变量 必须放在赋值之前否咋报错
    #v=300

    #v+=200 #找不到局部变量V导致报错 因为你不能修改全局的变量 所以报找不到  如果你非要修改外面的V，你声明这个就是全局的

f1()
print(v)
