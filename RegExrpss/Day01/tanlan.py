# -*- coding:utf-8 -*-
import re
s = '''
<div>扬天大笑出门去</div>
<div>九霄龙吟惊天变</div>
'''

#贪婪匹配
result=re.findall('<div>[\s\S]*</div>',s) #因为\n 也是\s\S 所以一直匹配到尾巴
print(result)

#非贪婪匹配
result2=re.findall('<div>([\s\S]*?)</div>',s) #找到第一个</div>就结束
print(result2)