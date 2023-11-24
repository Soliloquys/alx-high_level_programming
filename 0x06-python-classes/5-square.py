#!/usr/bin/python3
"""Defines a class called Square"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize a new Square
        Args:
            size(int): the size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        """Get the current size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not  isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        Area = (self.__size ** 2)
        return Area
    
    def my_print(self):
        """Print the number of square with #"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
            if self.__size = 0:
                print("")
