#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """exception raise"""

    def area(self):
        raise Exception("area() is not implemented")
    
    """method integer_validator, this method uses raises for validating"""

    def integer_validator(self, name, value):
        if not isinstance(int, value):
            raise TypeError(f"{value} must be an integer")
        if value <= 0:
            return ValueError(f"{value} must be greater than 0")

