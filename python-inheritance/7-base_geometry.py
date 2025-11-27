#!/usr/bin/python3
"""Integer validator"""


class BaseGeometry:
    """exception raise"""

    def area(self):
        raise Exception("area() is not implemented")
    
    """method integer_validator, this method uses raises for validating"""

    def integer_validator(self, name, value):
        if type(int) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            return ValueError("{} must be greater than 0".format(name))

