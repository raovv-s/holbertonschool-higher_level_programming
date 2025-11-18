#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    list = [int(arg) for arg in sys.argv[1:]]
    s = 0 
    for i in (list):
        s += i
    print (s)
