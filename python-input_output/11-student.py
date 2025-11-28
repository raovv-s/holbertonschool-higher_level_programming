#!/usr/bin/python3
"""Student Class with json function"""


class Student:
    """Class Student with init and to_json function"""

    def __init__(self, first_name, last_name, age):
        """init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""

        if isinstance(attrs, list):

            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """function which reloads json"""

        for key, value in json.items():
            setattr(self, key, value)
