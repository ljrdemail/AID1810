def get_chinese_char_count(s):
    count = 0
    for x in str:

        if (int("0x4E00", base=16) <= ord(x) <= int("0x9FA5", base=16)):
            count += 1
    return count


str = input("请输入中英文混杂的字符:")
print(get_chinese_char_count(str))
