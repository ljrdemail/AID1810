height=float(input("请输入身高（米）："))
weight=float(input("请输入体重（公斤）："))

BMI=round(weight/height**2,2)

if (BMI<18.5):
    print(BMI)
    print("你体重过轻")
elif (18.5<=BMI<=24):
    print(BMI)
    print("你体重正常")
else:
    print(BMI)
    print("你体重过重")