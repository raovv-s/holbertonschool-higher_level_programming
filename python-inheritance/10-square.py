#!/usr/bin/python3
"""Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting Rectangle"""

    def __init__(self, size):

        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """area of square"""

        return self.__size * self.__size
    def __str__(self):
        """String representation of rectangle"""
        return f"[Rectangle] {self.__size}/{self.__size}"
