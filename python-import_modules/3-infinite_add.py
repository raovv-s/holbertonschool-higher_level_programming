#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    numbers = [int(arg) for arg in sys.argv[1:]]
    s = 0
    for i in numbers:
        s += i
    print(s)
