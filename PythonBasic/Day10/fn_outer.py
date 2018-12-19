def fn_outer():
    print("fn_outer调用开始....")
    i=100
    def fn_inner():
        print(" fn_inner 被调用")
        print(i)

    fn_inner()
    fn_inner()

    print("fn_outer调用结束....")


fn_outer()
