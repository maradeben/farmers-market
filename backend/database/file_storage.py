""" implement initial storage """
import json
from backend.models.product import products_list


db_file_path = './database/store.db'

class FileStorage:
    """ Rudimentary file storage """
    __file_path  ='./backend/database/store.json'
    __objects = {}

    def save(self):
        objs = {key: val for key,val in products_list.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objs, f)
    
    def all(self):
        """ retrieve all objects """
        with open(self.__file_path, 'r', encoding="utf-8") as f:
           self.__objects = json.load(f)
        return self.__objects

file_store = FileStorage()