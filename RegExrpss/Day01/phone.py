import re

s = "hello 13267102743 I am 13632651973,He is 119 hello 119"
rlist = re.findall('\d{11}', s)
rlist2 = re.findall('hello', s) #不一定是含有特殊含义的 元字符
print(rlist)
print(rlist2)
