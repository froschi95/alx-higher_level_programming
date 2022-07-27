#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    item = 0
    for i in range(0, list_length):
        try:
            item = my_list_1[i] / my_list_2[i]
        except TypeError:
            item = 0
            print("wrong type")
        except ZeroDivisionError:
            item = 0
            print("division by 0")
        except IndexError:
            item = 0
            print("out of range")
        finally:
            pass
        res.append(item)
    return res
