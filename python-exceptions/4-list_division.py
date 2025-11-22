#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    s = 0
    new_list = []
    for i in range(list_length):
        try:
            s = my_list_1[i] / my_list_2[i]
            new_list.append(s)
        except ZeroDivisionError:
            print("division by 0")
            s = 0
        except TypeError:
            print("wrong type")
            s = 0
        except IndexError:
            print("out of range")
            s = 0
        finally:
            new_list.append(s)
    return new_list