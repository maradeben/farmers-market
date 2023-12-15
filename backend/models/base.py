#!/usr/bin/env python3.9
""" Define the base model for other models, including users, vendors, and products """
from datetime import datetime
from uuid import uuid4


time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """ BaseModel class, template for creating all objects
    Attributes:
        id (str): a uuid4 unique id auto generated whenever a new object is created
        created_at: (datetime.datetime): timestamp of object creation
    
    Methods:
        save(): save the object
        delete(): delete the object
    """

    def __init__(self):
        """ Initialization function to create id and timestamp """
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
    
    def __str__(self):
        return (f"{self.__class__}: {self.id}-{self.created_at}")
    
    def to_dict(self):
        the_dict = self.__dict__
        if 'created_at' in the_dict and not isinstance(the_dict['created_at'], str):
            the_dict['created_at'] = the_dict['created_at'].strftime(time)
        the_dict['object'] = self.__class__.__name__
        return self.__dict__
