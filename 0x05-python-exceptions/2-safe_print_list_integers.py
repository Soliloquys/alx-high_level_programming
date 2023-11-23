#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}".format(int(my_list[i])), end="")
                count += 1
    except ValueError:
        pass
    finally:
        print()
    return count
