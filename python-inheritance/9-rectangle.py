#!/usr/bin/python3
"""Rectangle Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """init method"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
    
    """area method"""

    @property
    def area(self, width, height):
        return __width * __height
    
    """print method"""

    @property
    def __str(self, width, height):
        return(f"[Rectangle] {__width}/{__height}")
    
    """print method"""

