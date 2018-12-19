import re

s = "3049@qq.comwang@126.comwei@163.commeng@tedu.cn"
com = re.findall("[a-zA-Z0-9@]+.com", s)
# com=re.findall("\w+@\w+\.com",s)

print(com)

reg = "[a-zA-Z0-9@]+.com|[a-zA-Z0-9@]+.cn"
reg2 = "\w+@\w+\.com|\w+@\w+\.cn"

comcn = re.findall(reg2, s)
print(comcn)
