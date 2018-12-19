'''
这是games子包里的文件


'''

print("mypack/games/__init__.py 被加载")

__all__=['contra','tanks']
#会影响from mypack.games improt *
# 当上述语句导入的时候 只导入contra 和thanks
# 默认所有的包内模块都不导入