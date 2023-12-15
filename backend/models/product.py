""" Module containing blueprint for product """
from models.base import BaseModel
import sys


product_categories =  ['Grains', 'Roots/Tubers', 'Fruits/Vegetables', 'Meat/Poultry', 'Oils']

class Product(BaseModel):
    """ Product template class, inheriting from the BaseModel

    Attributes:
        Inhertied: id, created_at -> from BaseModel
        name(str): product name
        category(str): category of the product
        price(float): price of product
        qty(int): quantity in stock
        vendor(str): the seller of the product
        rating(str): product rating
    
    Methods:
    """

    def __init__(self, name: str=None, category: str=None, price: float=None, qty: int=None,
                  vendor_id: str=None, **kwargs) -> None:
        """ Initializing function """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'name':
                    name = kwargs.get('name')
                elif key == 'category':
                    category = kwargs.get('category')
                elif key == 'price':
                    price = kwargs.get('price')
                elif key == 'qty':
                    qty = kwargs.get('qty')
                elif key == 'vendor_id':
                    vendor_id = kwargs.get('vendor_id')
                else:
                    print(f"Invalid Product attribute: {key}")
                    return
        else:
            if not all([name, category, price, qty, vendor_id]):
                print("Incomplete values")
                return
            if not isinstance(name, str):
                print("Product name must be of type 'str'")
                return
            if not isinstance(category, str) or category not in product_categories:
                print(f"Invalid Product category: {category}")
                return
            if not isinstance(price, (int, float)):
                print("Product price must be of type 'int' or 'float'")
                return
            if not isinstance(qty, int):
                print("Product quantity must be of type 'int'")
                return
            if not isinstance(vendor_id, str):
                print("Product vendor id must be of type 'str'")
                return

        super().__init__()
        self.name = name
        self.category = category
        self.__price = price
        self.__qty = qty
        self.vendor_id = vendor_id
        self.rating = 0 # rating is initially 0
    
    # getter for price
    @property
    def price(self):
        """ return the price """
        return self.__price
    
    # setter for price
    @price.setter
    def price(self, price):
        """ update price """
        if not price or not isinstance(price, (int, float)):
            print("Invalid Product price")
            return
        self.__price = price
    
    # getter for quantity
    @property
    def qty(self):
        """ return the quantity """
        return self.__qty
    
    # setter for quantity
    @qty.setter
    def qty(self, quantity):
        if not quantity or not isinstance(quantity, int):
            print("invalid Product quantity")
            return
        self.__qty = quantity
