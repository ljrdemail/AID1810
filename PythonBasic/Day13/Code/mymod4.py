'''

_下划线开头的方法和变量不会被导入

'''

def f():
    pass


def _f1():
    pass


def f2():
    pass


name1 = 'aaaaaa'
__name1 = "bbbbbb"
