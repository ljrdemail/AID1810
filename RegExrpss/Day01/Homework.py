# -*- coding:utf-8 -*-
import re

s = """
<div class="动物">
    <p class="名字">
        <a title="兔子"></a>
    </p>
    <p class="描述">
    小白兔,白又白,两只耳朵竖起来
  </p>
</div>
<div class="动物">
    <p class="名字">
        <a title="老虎"></a>
    </p>
    <p class="描述">
     两只老虎两只老虎跑的快跑的快
  </p>
</div>
"""
regex = re.compile('<div class="动物">.*?title="(.*?)".*?描述">(.*?)</p>',
                   re.S)  # re.S 让.能替代\n  .*? 加了? 代表到后续的比如title 就不再往后取了否则* 可以代表任意字符
rlist = regex.findall(s)
# print(rlist)
for r in rlist:
    print("动物名称：%s" % r[0].strip())
    print("动物描述：%s" % r[1].strip())
    print("*" * 40)
