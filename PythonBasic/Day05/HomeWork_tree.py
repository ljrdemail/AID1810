sg = int(input("请输入圣诞树树干长度："))
stars = 1
for i in range(sg):
    print((' ' * (sg - i)) + ('*' * stars))
    stars += 2
for j in range(sg):
    print((' ' * (sg)) + '*')
