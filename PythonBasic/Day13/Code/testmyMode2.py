import mymod
import pdb

'''
此模块将作为主模块来导入mymod模块
用mymod里的函数和数据 组成我的程序



'''

mymod.__doc__
name1="华为"#和mymod里面的 不冲突 即是你导入了 因为变量仅限于 模块内部
name2="小米"


print(name1)
print(mymod.name1)
print("testmode2也有自己的名字",__name__) #第一个进来的去调用别人的 模块一定叫__main__而不是 test2
print("testmode2也有自己的路径",__file__)