""" Module containing blueprint for product """
from models.base import BaseModel
import sys
from typing import Union


product_categories =  ['Grains', 'Roots/Tubers', 'Fruits/Vegetables', 'Meat/Poultry', 'Oils']
products_list = []

class Product(BaseModel):
    """ Product template class, inheriting from the BaseModel

    Attributes:
        Inhertied: id, created_at -> from BaseModel
        name(str): product name
        category(str): category of the product
        price(float): price of product
        stock(int): quantity in stock
        vendor(str): the seller of the product
        rating(float): product rating
    
    Methods:
    """

    def __init__(self, name: str=None, category: str=None, price: float=None, stock: int=None,
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
                elif key == 'stock':
                    stock = kwargs.get('stock')
                elif key == 'vendor_id':
                    vendor_id = kwargs.get('vendor_id')
                else:
                    print(f"Invalid Product attribute: {key}")
                    return
        else:
            if not all([name, category, price, stock, vendor_id]):
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
            if not isinstance(stock, int):
                print("Product stock must be of type 'int'")
                return
            if not isinstance(vendor_id, str):
                print("Product vendor id must be of type 'str'")
                return

        super().__init__()
        self.name = name
        self.category = category
        self.__price = price
        self.__stock = stock
        self.vendor_id = vendor_id
        self.__rating = 0 # rating is initially 0
        self.no_ratings = 0
    
    # getter for price
    @property
    def price(self):
        """ return the price """
        return self.__price
    
    # setter for price
    @price.setter
    def price(self, price: Union[int, float]):
        """ update price """
        if not price or not isinstance(price, (int, float)):
            print("Invalid Product price")
            return
        self.__price = price
    
    # getter for quantity
    @property
    def stock(self):
        """ return the quantity """
        return self.__stock
    
    # setter for quantity
    @stock.setter
    def stock(self, quantity: int):
        if not quantity or not isinstance(quantity, int):
            print("invalid Product quantity")
            return
        self.__stock = quantity
    
    # decrement quantity on purchase
    def decr_stock(self, count: int) -> int:
        """ Reduce the quantity of product remaining in stock
        Args:
            count(int): the count of product purchased
        
        Return:
            remaining stock
        """
        if count > self.__stock:
            print(f"Insufficient stock. Only {self.__stock} units available")
            return
        self.__stock -= count
        self.stock
        # save updates
        self.save()
    
    # increament quantity on addition of new stock
    def incr_stock(self, count: int) -> int:
        """ opposite of decr_quantity, add to stock """
        self.__stock += count
        self.stock
        # save updates
        self.save()

    # getter for rating
    @property
    def rating(self):
        """ return rating """
        return self.__rating
    
    def update_rating(self, new_rating) -> float:
        """ update rating when new rating is added 
        Args:
            new_rating(int): the new rating
        
        Return:
            the new average rating
        """
        # compute new average rating
        self.__rating = ((self.no_ratings * self.__rating) + new_rating) / (self.no_ratings + 1)
        # increment no of ratings
        self.no_ratings += 1
        self.rating
        # save updates
        self.save()
    
    # save the product
    def save(self):
        products_list.append(self.to_dict())
