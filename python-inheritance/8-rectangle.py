#!/usr/bin/python3
from 7-base_geometry import *
"""Rectangle Class"""


class Rectangle(BaseGeometry):
    """init method"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
