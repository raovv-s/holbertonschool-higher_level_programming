#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if(len(sys.argv) == 0):
        print(f"{len(sys.argv)} arguments.")
        sys.exit()
    if(len(sys.argv) > 0):
        print(f"{len(sys.argv)} arguments.")
    for i in range(1,len(sys.argv)):
        a = sys.argv[i]
        print(f"{i}: {a}")
