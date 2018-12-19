# -*- coding:utf-8 -*-
import re

# re.findall()
pattern = r'\w+:\d+'
s = '金毛狮王:1950 紫衫龙王:1949'
rlist = re.findall(pattern, s)
print(rlist)

# reges.findall()
regex = re.compile(pattern, flags=0)
# rlist2 = regex.findall(s,pos=0,endpos=len(s))
# pos 目标字符串起始值，endpos 目标字符串终止值
rlist2 = regex.findall(s, pos=0, endpos=11)
print(rlist2)

# spilit() 方法
regex = re.compile("\s+")
rSplit = regex.split("hello world hi python")
print(rSplit)

# sub()方法
regex = re.compile(r"\s+")
# rSub = regex.sub('###', 'Hello World Python', 1)  # 把第一个空格替换为###
# rSub = regex.sub('###', 'Hello World Python', 2)
rSub = regex.sub('###', 'Hello World Python', 0)  # 0 是默认全替换
print(rSub)

# subn()方法
regex = re.compile(r"\s+")
# rSub = regex.sub('###', 'Hello World Python', 1)  # 把第一个空格替换为###
# rSub = regex.sub('###', 'Hello World Python', 2)
rSub = regex.subn('###', 'Hello World Python', 0)  # 0 是默认全替换
print(rSub)

# finditer(） 方法
rIter = re.finditer(r"\d+", "2019来了,2018啥也没干")  # 结果为迭代器 遍历出来的是match 对象  利用match对象的group 方法 拿到匹配的内容
# print(rIter)
for x in rIter:
    print(x.group())

# match(）方法
try:
    rMatch = re.match(r'[A-Z]\w+', 'Hello world')
    print(rMatch.group())  # 只匹配行首 H m满足[A-Z] ello满足w+ 空格不满足 停止
# 如果找不到返回不了对象 要用 try except 处理
except Exception as e:  # hello world' 就会报错
    print(e)
    print("没有匹配到内容")

# search()方法

try:
    rSerch = re.search(r'\d+', "hello 123 i am 456")
    print(rSerch.group())
except Exception as e:
    print(e)
    print("没有匹配到内容")

# fullmatch 完整匹配
try:
    rFull = re.fullmatch(r'\w+', 'hello2019')
    # rFull = re.fullmatch(r'\w+', 'hello 2019')
    # r'^\w+$'
    print(rFull.group())
except Exception as e:
    print(e)
    print("没有匹配到内容")

# match 对象的方法
rGroup = re.search(r'(?P<tiger>\w+)\s+(?P<lion>\w+)', "A B C D")
# print(rGroup.group())
# print(rGroup.group(1))
# print(rGroup.group(2))
# print(rGroup.group("tiger"))
# print(rGroup.group("lion"))
#print(rGroup.groups())
print(rGroup.groupdict())

print(rGroup.span()) #其实是第二位因为终值取不到 所以往后推一位3  "A B C D")
print(rGroup.start())
print(rGroup.end())
