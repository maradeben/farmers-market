""" Module containing blueprint for product """
from mongoengine import DynamicDocument, IntField, StringField, ReferenceField,\
    DateTimeField, FloatField, EmailField, ListField
from models.vendor import Vendor
from backend.database import file_store
import sys
from typing import Union
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError


product_categories =  ['Grains', 'Roots/Tubers', 'Fruits/Vegetables', 'Meat/Poultry', 'Oils']

class Product(BaseModel, DynamicDocument):
    """ Product template class, inheriting from the BaseModel

    Attributes:
        Inhertied: id, created_at -> from BaseModel
        name(str): product name
        category(str): category of the product
        price(float): price of product
        unit(str): unit of measurement, e.g., bag, kg
        stock(int): quantity in stock
        vendor_id(str): the seller of the product
        rating(float): product rating
        location(str): the location of the product, based on vendor's location
        image(str): path to the image
    
    Methods:
    """

    name = StringField(required=True)
    price = FloatField(required=True)
    unit = StringField(required=True)
    category = StringField(required=True)
    stock = IntField(required=True)
    vendor = ReferenceField(Vendor, required=True)
    rating = FloatField(required=True)
    num_ratings = IntField(required=True, default=0)
    image_url = ListField(StringField(), required=True,
            default=['frontend/assets/images/product-images/default-product-image.jpg'])
    
    meta = {
        'collection': 'products'
    }


    # override init function to accomodate auto-saving on creation
    def __init__(self, **kwargs):
        # default init to create the object
        super(Product, self).__init__(**kwargs)
        self.save()




    # these are only for file storage
    if 0:
        def __init__(self, **kwargs) -> None:
            """ Initializing function """
            if kwargs:
                for key, value in kwargs.items():
                    if key == 'name':
                        name = value
                    elif key == 'category':
                        category = value
                    elif key == 'price':
                        price = value
                    elif key == 'unit':
                        unit = value
                    elif key == 'stock':
                        stock = value
                    elif key == 'vendor_id':
                        vendor_id = value
                    elif key == 'rating':
                        rating = value
                    elif key == 'image_url':
                        image_url = value
                    else:
                        raise AttributeError(f"Invalid Product attribute: {key}")
                    
            if not all([name, category, price, unit, stock, vendor_id, rating]):
                raise ValueError("Incomplete values")
            if not isinstance(name, str):
                raise TypeError("Product name must be of type 'str'")
            if not isinstance(category, str):
                raise TypeError("Product category must be of type 'str")
            if category not in product_categories:
                raise ValueError(f"Invalid Product category: {category}")
            if not isinstance(price, (int, float)):
                raise TypeError("Product price must be of type 'int' or 'float'")
            if not isinstance(unit, str):
                raise TypeError("Product unit must be of type 'str'")
            if not isinstance(stock, int):
                raise TypeError("Product stock must be of type 'int'")
            if not isinstance(vendor_id, str):
                raise TypeError("Product vendor id must be of type 'str'")
            if not isinstance(rating, float):
                raise TypeError("Product rating must be of type 'int'")
            if not isinstance(image_url, str):
                raise(TypeError("Product image_url path must be of type 'str'"))

            super().__init__()
            self.name = name
            self.category = category
            self.__price = price
            self.unit = unit
            self.__stock = stock
            self.vendor_id = vendor_id
            self.__rating = rating # rating is initially 0
            self.num_ratings = 0
            self.location = self.get_location()
            self.image_url = image_url

            # print('\n\nInitializing...', self.id)
            self.save()
        

        def save(self):
            """ save a newly initialized product """

            key = self.id
            # print('\n\nSaving', self.id)
            # construct a token from name, category, and vendor_id
            token = f"{self.name}-{self.category}-{self.vendor_id}"
            all_objects = file_store.all()
            if all_objects and all_objects['products']:
                products = all_objects['products']
                all_tokens = [f"{value['name']}-{value['category']}-{value['vendor_id']}"\
                                for key, value in products.items()]
                if token in all_tokens:
                    return("Product exists. Update instead")
                else:
                    file_store.all_products[key] = self.to_dict()
            else:
                file_store.all_products[key] = self.to_dict()


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
                raise TypeError("Invalid Product price")
            self.__price = price
            # save new price
            self.update()
        
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
            # save new stocks
            self.update()
        
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
            self.update()
        
        # increament quantity on addition of new stock
        def incr_stock(self, count: int) -> int:
            """ opposite of decr_quantity, add to stock """
            self.__stock += count
            self.stock
            # save updates
            self.update()

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
            self.__rating = ((self.num_ratings * self.__rating) + new_rating) / (self.num_ratings + 1)
            # increment no of ratings
            self.num_ratings += 1
            self.rating
            # save updates
            self.update()
        
        def get_location(self):
            """ retrieve the location of a product, which is the location of the vendor """
            vendor = file_store.get_single_vendor(self.vendor_id)
            return vendor['location']
