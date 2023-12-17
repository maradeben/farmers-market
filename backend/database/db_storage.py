#!/usr/bin/python3 
"""Contains the DB Storage"""


import mongoengine
from os import environ

class DBStorage:
    """Interacts with MongoDB Database
    Adopting Singleton connection to prevent multiple connections
    """


    _instance = None
    db_name = environ.get('DB_NAME', 'farmer_market')
    host = environ.get('HOST', '127.0.0.1')
    port = int(environ.get('PORT', '27017'))
    meta = {'db_alias': 'core'}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(DB_Store, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance
    
    @classmethod
    def connect(cls):
        mongoengine.register_connection(alias='core', name=cls.db_name, host=cls.host, port=cls.port)
        mongoengine.connect(cls.db_name, alias='core')

    @classmethod
    def close_connection(cls):
        mongoengine.disconnect(cls.db_name)


engine = DB_Store()
