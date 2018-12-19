# -*- coding:utf-8 -*-


def BinarySearch(arr, key):
    # 记录数组的最高位和最低位
    min = 0
    max = len(arr) - 1

    if key in arr:
        # 建立一个死循环，直到找到key
        while True:
            # 得到中位数
            # 这里一定要加int，防止列表是偶数的时候出现浮点数据
            center = int((min + max) / 2)
            # key在数组左边
            if arr[center] > key:
                max = center - 1
            # key在数组右边
            elif arr[center] < key:
                min = center + 1
            # key在数组中间
            elif arr[center] == key:
                print(str(key) + " 在数组里面的第" + str(center) + "个位置")
                return arr[center]
    else:
        print("没有该数字!")


list = [x for x in range(1, 14)]
print(list)

while True:
    key = input("请输入你要查找的数字：")
    if key == " ":
        print("谢谢使用！")
        break
    else:
        BinarySearch(list, int(key))
