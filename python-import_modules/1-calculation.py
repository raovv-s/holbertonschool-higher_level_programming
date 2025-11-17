#!/usr/bin/python3

if __name__ == '__main__':
    from add_0 import add, sum, mul, div
    a = 10
    b = 5
    def ls():
        print("{} + {} = {}".format(a, b, add(a, b)))
        print("{} + {} = {}".format(a, b, sum(a, b)))
        print("{} + {} = {}".format(a, b, mul(a, b)))
        print("{} + {} = {}".format(a, b, div(a, b)))
    ls()
