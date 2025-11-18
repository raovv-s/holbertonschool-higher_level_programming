#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argv = sys.argv[1:]
    c = len(argv)
    if c ==  0:
        print(f"{c} arguments")
    else:
        if c == 1:
          print(f"{c} argument")
        else:
            print(f"{c} arguments")
        for i in range(c):
          print(f"{i+1}: {argv[i]}")
