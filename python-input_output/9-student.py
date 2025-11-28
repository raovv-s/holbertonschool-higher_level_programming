#!/usr/bin/python3
"""Student Class with json function"""

class Student:
    """Class Student with init and to_json function"""

    def __init__(self, first_name, last_name, age):
        """init"""

        self.first_name = first_name
        self.last_name = last_name 
        self.age = age
    
    def to_json(self):
        """to json"""
        
        return self.__dict__
