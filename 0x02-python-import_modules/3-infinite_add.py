#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = 0
    lenArg = len(sys.argv)
    for i in range(1, lenArg):
        arg = int(sys.argv[i])
        total += arg
    if lenArg > 1:
        print("{}".format(total))
