for x in range(4, 0):
    print(x)
else:
    print("else子句中x=",x) #x 也没有 也会报错
print("循环结束之后的x 的值是", x)  # 出错 因为变量x不存在 因为range返回的对象为空 无法赋值给x
