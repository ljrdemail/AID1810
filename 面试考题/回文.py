# 思路 原字符串 反转 后等于源字符串则是回文
#s2=s1[::-1] 反转后用s2绑定

str = input("请输入需要判断是否为回文的字符：")
#上海自来水来自海上
# a = str[0:(len(str) // 2)]
# b = str[:(len(str) // 2) - 1:-1]

str2=str[::-1]

#if (a == b):
if (str == str2):
    print("是回文")
else:
    print("不是回文")
