import re

s = "hello 13267102743 I am 13632651973,He is 119 hello 119"
rlist = re.findall('\d{11}', s)
rlist2 = re.findall('hello', s) #��һ���Ǻ������⺬��� Ԫ�ַ�
print(rlist)
print(rlist2)
