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
            cls._instance = super(DBStorage, cls).__new__(cls)
            cls._instance.connect()
        return cls._instance
    
    @classmethod
    def connect(cls):
        mongoengine.register_connection(alias='default', name=cls.db_name, host=cls.host, port=cls.port)
        mongoengine.connect(cls.db_name, alias='default')

    @classmethod
    def close_connection(cls):
        mongoengine.disconnect(alias='default')
    
    @classmethod
    def clear_storage(cls):
        """ clear the database """
        mongoengine.disconnect(alias='core')
        cls.connect()  # reconnect if needed
        mongoengine.connection.get_connection().drop_database(cls.db_name)
        cls.close_connection()


storage_engine = DBStorage()
