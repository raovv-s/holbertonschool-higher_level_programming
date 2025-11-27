#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """exception raise"""

    def area(self):
        raise Exception("area() is not implemented")
    
    """method integer_validator, this method uses raises for validating"""

    def integer_validator(self, name, value):
        if type(int) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            return ValueError(f"{name} must be greater than 0")
