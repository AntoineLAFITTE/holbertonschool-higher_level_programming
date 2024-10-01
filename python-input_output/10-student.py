#!/usr/bin/python3
"""Module containing the Student class"""

class Student:
    """Defines a student with first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of the Student instance.

        If attrs is a list of strings, only those attributes listed in
        attrs are retrieved. Otherwise, all attributes are returned.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
            Defaults to None.

        Returns:
            dict: A dictionary containing the specified attributes
            or all attributes.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        return self.__dict__
