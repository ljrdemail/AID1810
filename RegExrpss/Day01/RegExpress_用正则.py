import re

s = "70559506@qq.com peter@126.com 12345678@qq.com"

qq = re.findall("\d+@qq.com", s)  # findAll����һ���б�

print(qq)
