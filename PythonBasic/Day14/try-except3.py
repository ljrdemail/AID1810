def div_apple(n):  # 分苹果
    print("现在有%d个苹果，你想分给几个人" % n)
    s = input("请输入人数：")
    cut = int(s)  # 此处可能会触发ValueError 类型的错误
    result = n / cut  # 此处也有可能触发ZeroDivisionError
    print("每个人分了", result, '个苹果')


try:
    print("开始分苹果！！")
    div_apple(10)
    print("分苹果完成")
except (ValueError,ZeroDivisionError) as err: #兜底处理逻辑 其他except处理不了的 放在这里
    print("分苹果失败，苹果不分了") #是一个元组
    print("错误原因是：",err)
# except ValueError as err :
#   print("分苹果时候数字输入错误，苹果被收回！")
#   print("引起错误的原因是:",err)
# except ZeroDivisionError as err2:
#   print("分苹果时候数字输入为0，苹果被收回！")
#   print("引起错误的原因是:", err2)

print("程序结束")
