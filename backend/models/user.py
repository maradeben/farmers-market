""" Module containing blueprint for user """
from mongoengine import DynamicDocument, EmbeddedDocument, EmbeddedDocumentField,\
    IntField, StringField, ReferenceField, DateTimeField, FloatField, EmailField, ListField
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError
from flask_login import UserMixin

from backend.custom_errors import *

import datetime

class User(DynamicDocument, UserMixin):
    """ User model
    Inherits from UserMixin to provide default attributes for flask_login
    Attrs:
        phone(str): phone number
        email(str): email
        firstname(str)
        lastname(str)
        username(str)
        password(bytes): hashed password
        role(str): defaults to user
        cart(list): to hold products added to cart
        created_at(datetime): time of creation
    
    Methods:
    """
    phone = StringField()
    email = EmailField(required=True, unique=True)
    firstname = StringField(required=True)
    lastname = StringField(required=True)
    username = StringField()
    password = StringField(required=True)
    role = StringField(default='user')
    cart = ListField(ListField())
    created_at = DateTimeField(required=True, default=datetime.datetime.now())

    meta = {
        'collection': 'users',
        "allow_inheritance": True
    }


def register_user(**kwargs):
    """ bundle registration of a User """

    # importing here to prevent circular import
    from backend.models.vendor import Vendor

    user = User(**kwargs)
    try:
        user.save()
    except(DuplicateKeyError, NotUniqueError):
        profile = Vendor.objects(email=kwargs['email'])
        if profile:
            raise DuplicateVendorError(f"Error: {user.email} is already registered as a Vendor") from None
                # print("Duplicate product")
        print(f"Error: {user.email} is previously registered")
        raise
        # print("User exists")
    else:
        print(f"{user.email} sucessfully registered")
        # pass
    return user

