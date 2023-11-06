#!/usr/bin/python3
"""
Module 10-square.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inheriting from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square instance.
        Args:
            size (int): the size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Return the square description in the format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
