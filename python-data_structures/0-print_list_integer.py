#!/usr/bin/python3
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]

    def print_list_integer(my_list=[]):
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i])) 

    print_list_integer(my_list)