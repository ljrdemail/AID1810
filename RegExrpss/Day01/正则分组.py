# -*- coding:utf-8 -*-
import re

s = 'A B C D'

r1 = re.findall('\w+\s+\w+', s)
print(r1)

r2 = re.findall('(\w+)\s+\w+', s)
print(r2)
# 第一步：['A B', 'C D'] 整体匹配
# 第二步 ['A', 'C'] 在第一步的基础上每组拿出打括号的值 这里是 A 和  C

r3 = re.findall('(\w+)\s+(\w+)', s)
# 第一步 先按整个表达式匹配  ['A B', 'C D']
# 第二步 [(A,B),{C,D}]谁加括号放列表 \s 没有打括号 所以不放 所以第一组放 A B 后面一组 放C D 如果有多个分组则每个分组用元组形式存放于列表中
print(r3)

r4=re.findall('((\w+)\s+)(\w+)',s) # 从外向内 从左向右

print(r4)
#第一组 （(\w+)\s+）

#第二组 （\w+）
#第三组  (\w+)（后面哪个）

#第一步  ['A B', 'C D']
#第二步 看第一组加括号  ['A ' 'C ']  因为第一个加括号 有空格
        # 看第二组      ['A ' 'C'] 没空格
        #看第三组     [B D]
#放进元组
   # 1   2    3 组
 #[('A ','A','B')]
 #后面同理[{C,C,D}]

