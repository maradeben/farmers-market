#!/usr/bin/env python3
""" Set up basic template for a vendor """
from backend.models.base import BaseModel
from backend.database import file_store
import mongoengine 


class Vendor(BaseModel):
    """ Template for the vendor

    Attrs:
        Inherited: id, created_at
        rating(float): vendor rating
        no_ratings(float): number of times vendor has been rated
        email(str): vendor email, will be used as unique identifier
        phone(str): phone
        first_name(str): first name
        last_name(str): last name
        username(str): user name
    
    Methods:

    """
 
    phone = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)
    firstname = mongoengine.StringField(required=True)
    lastname = mongoengine.StringField(required=True)
    username = mongoengine.StringField(required=True)
    farmname = mongoengine.StringField(required=True)
    location = mongoengine.StringField(required=True)
    meta = {
        'db_alias': 'core',
        'collection': 'vendors'
    }

    def __init__(self, **kwargs):
        """ initialize a Vendor. Can be done by passing positional arguments,
        or by passing a dict of keyword arguments"""

        if kwargs:
            for key, value in kwargs.items():
                if key == 'phone':
                    phone = value
                elif key == 'email':
                    email = value
                elif key == 'first_name':
                    firstname = value
                elif key == 'last_name':
                    lastname = value
                elif key == 'username':
                    username = value
                elif key == 'farmname':
                    farmname = value
                elif key == 'location':
                    location = value
                else:
                    raise ValueError("Invalid Vendor parameter")

        if not all([phone, email, firstname, lastname, username, farmname, location]):
            raise ValueError("Incomplete credentials")
        
        if not all(isinstance(var, str) for var in (phone, email, firstname, lastname, username, farmname, location)):
            raise TypeError("Invalid type entered for vendor parameter. Must be string")
    
        super().__init__()
        self.rating = 0
        self.num_ratings = 0
        self.phone = phone
        self.email = email
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.farmname = farmname
        self.location = location

        self.save()
    
    def save(self):
        """ save newly initialized object, ensuring it is not previously existing """
        key = self.id
        # construct a token from email and lastname
        token = f"{self.email}-{self.lastname}"
        all_objects = file_store.all()
        if all_objects and all_objects['vendors']:
            vendors = all_objects['vendors']
            all_tokens = [f"{value['email']}-{value['lastname']}" for key, value in vendors.items()]
            if token in all_tokens:
                return("Vendor profile exists. Log in instead")
            else:
                file_store.all_vendors[key] = self.to_dict()
        else:
            file_store.all_vendors[key] = self.to_dict()
