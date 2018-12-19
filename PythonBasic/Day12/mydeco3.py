# 假设银行系统有的业务为存钱和取钱

def privileged_check(fn):
    def fx(n, x):  # 先传给手机壳
        print("正在验证权限......")
        fn(n, x)  # 再把套了壳的手机传给用户

    return fx

def message_send(fn):
    def fy(n,x):
        fn(n,x)
        print("正在发送短信给：",n)
    return fy

# -------------以下是魏老师写的代码
@privileged_check
def savemoney(name, x):
    # print("正在验证权限......")
    # if 权限通过: 你可以选择 在本函数就验证权限 也可以把验证权限的代码作为包装函数
    print(name, '存钱', x, '元')


@message_send #装饰是套了privileged_check 之后返回的函数  privileged_check 取调用原始的 withdraw 一层套一层
#装饰器可以带多层  手机壳多层包  但是注意 每层返回的是前一层已经包装过的 所以要注意顺序
@privileged_check
def withdraw(name, x):
    # print("正在验证权限......")
    # if 权限通过:
    print(name, '取钱', x, '元')


# ----------------------- 以下是调用小张写的程序

# print("正在验证权限......")
# if 权限通过:  #在调用的时候验证也可以
savemoney("小王", 200)
savemoney("小赵", 400)
withdraw("小李", 500)
