#!/usr/bin/python3

"""Defines a base model class"""


class Base:
    """Base Model.

    A base class for all other classes

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes an instance of the class

        Args: id (int): the identity of the new instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
