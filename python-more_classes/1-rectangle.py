#!/usr/bin/python3
class Rectangle:
    """Rectangle class with private width attribute."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle with width and height."""
        self.__width = width  
        self.__height = height  
    
    @property
    def width(self):
        """Retrieve the width."""
        return self.__width

    def width(self, value):
        """Set the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    
    def height(self):
        return self.__height
    
    def height(self, height):
        """Set the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
