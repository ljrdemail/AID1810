# -*- coding:utf-8 -*-
import re

str = '''
<div class="desc"> 段子1 </div>
<div class="desc"> 段子2 </div>




'''

rlist = re.findall('<div class="desc">(.*?)</div>', str)  # . 任意字符 * 出现0此或一次 不加括号全部打印
#rlist = re.findall('<div class="desc">.*?</div>', str)
for i in rlist:
    print(i.strip())
