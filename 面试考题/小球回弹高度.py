def tanqi():
    sum = 0
    height = 100
    for i in range(1, 11):
        height *= 0.5
        print("第%d次回弹高度为%.2f" % (i, height))
        sum += 3 * height
        print("累计已经走过的路为", sum)
    return [sum, height]


tanqi = tanqi()

print("第10次回弹高度为:",tanqi[1])
print("第10次回弹后走过的路:",tanqi[0])
