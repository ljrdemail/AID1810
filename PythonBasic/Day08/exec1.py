jingli = {'曹操', '刘备', '孙权', }
jishu = {'曹操', '刘备', '张飞', '关羽'}

jj = jingli & jishu
print(jj)

j = jingli - jishu
print(j)

js = jishu - jingli
print(js)

zf = '张飞' in jingli
print(zf)

yz = (jingli ^ jishu)
print(yz)

gyjr = len(jingli | jishu)
print(gyjr)
