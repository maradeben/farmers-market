#!/usr/bin/env python3
""" Set up basic template for a vendor """
from mongoengine import DynamicDocument, EmbeddedDocument, EmbeddedDocumentField,\
        IntField, StringField, ReferenceField, DateTimeField, FloatField, EmailField, ListField
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError

from backend.custom_errors import *
from backend.models.user import User

import json
import datetime

class VendorInfo(EmbeddedDocument):
    """ Additional vendor specific details
    Attrs:
        farmname(str): name of the farm
        locaton(str): farmer/business location
        ratin(float): rating of the business
        num_ratings(int): number of times rated
    Methods:
    """

    farmname = StringField(required=True)
    location = StringField(required=True)
    rating = FloatField(default=0)
    num_ratings = IntField(default=0)
    


class Vendor(User):
    """ Vendor Module
    Attrs:
        vendor_details(VendorInfo): contains vendor specific details
            as defined in the VendorInfo EmbeddedDocument
        role(str): role of the vendor
    Methods:
    """
        
    vendor_details = EmbeddedDocumentField(VendorInfo, required=True)
    role = StringField(default='vendor')


def register_vendor(**kwargs):
    """ handle converting of a User to a Vendor """
    user_profile = User.objects(_cls="User", email=kwargs['email']).first()
    if user_profile:
        try:
            user_details = json.loads(user_profile.to_json())
            # don't reset created at, save the same created date
            created_at = datetime.datetime.utcfromtimestamp(
                            user_details.pop('created_at')['$date']/1000)
            # print(type(created_at), created_at)
            vendor = Vendor(**user_details)
            vendor.created_at = created_at
            # updated _clas attribute
            vendor._cls = 'User.Vendor'
            vendor.role = 'vendor'
            # remove email from the newly passed in data
            kwargs.pop('email')
            # add the additional vendor details
            vendor_info = VendorInfo(**kwargs)
            vendor.vendor_details = vendor_info
            # save the vendor and delete user profile
            user_profile.delete()
            vendor.save()
        except Exception:
            raise
        return vendor
    else:
        raise UserNotFoundError("User not found")


'''
______________________________________________________________________________________________________
______________________________________________________________________________________________________
______________________________________________________________________________________________________
______________________________________________________________________________________________________



    
    # these are functions only for file storage
    if 0:
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
                    elif key == 'rating':
                        rating = value
                    elif key == 'pswd':
                        pswd = value
                    else:
                        raise ValueError("Invalid Vendor parameter")

            if not all([phone, email, firstname, lastname, username, farmname, location, rating, pswd]):
                raise ValueError("Incomplete credentials")
            
            if not all(isinstance(var, str) for var in 
                        (phone, email, firstname, lastname, username, farmname, location, pswd)):
                raise TypeError("Invalid type entered for vendor parameter. Must be string")
            if not isinstance(rating, float):
                raise TypeError("Invalid type entered for vendor parameter 'rating'. Must be float")
        
            super().__init__()
            self.rating = rating
            self.num_ratings = 0
            self.phone = phone
            self.email = email
            self.firstname = firstname
            self.lastname = lastname
            self.username = username
            self.farmname = farmname
            self.location = location
            self.__pswd = pswd

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
'''