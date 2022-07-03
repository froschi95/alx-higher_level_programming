#!/usr/bin/python3
def uppercase(str):
    temp_lst = list(str)
    for i in range(len(temp_lst)):
        if ord(temp_lst[i]) > 96 and ord(temp_lst[i]) < 123:
            temp_lst[i] = chr(ord(temp_lst[i]) - 32)
    print("{}".format("".join(temp_lst)))
