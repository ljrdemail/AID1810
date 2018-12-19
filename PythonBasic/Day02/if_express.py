#商场促销 满100 减20

money=int(input("请输入商品总金额："))
pay=money-20 if money>=100 else money
print("你需要支付:",pay,"元")
