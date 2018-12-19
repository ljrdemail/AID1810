s = input("请输入字符串:")

b=bytearray(s,'utf-8')



print(len(s))
print(len(b))
#
s2=b.decode('utf-8')
print(s==s2)


