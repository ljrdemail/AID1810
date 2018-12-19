# -*- coding:utf-8 -*-
def recursion_search(data_source, find_n):
    mid = int(len(data_source) / 2)
    if len(data_source) >= 1:
        if find_n > data_source[mid]:
            recursion_search(data_source[mid + 1:], find_n)
        elif find_n < data_source[mid]:
            recursion_search(data_source[:mid], find_n)
        else:
            print(data_source[mid],"index：",mid)
    else:
        print("not found !")


if __name__ == '__main__':
    test_array = range(0, 100)
    recursion_search(test_array, 6)
