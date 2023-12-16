#!/usr/bin/python3 
"""Contains the DB Storage"""


import mongoengine
from models.base import BaseModel
from models.product import Product

class DBStorage:
    """Interacts with MongoDB Database"""

    def __init__(self):
        """Creating the db connecion"""
        mongoengine.register_connection(alias='core', name='farmer_market')

