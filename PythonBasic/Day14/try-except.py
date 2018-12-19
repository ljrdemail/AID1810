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
except ValueError:
  print("分苹果时候数字输入错误，苹果被收回！")
except ZeroDivisionError:
  print("分苹果时候数字输入为0，苹果被收回！")

print("程序结束")
