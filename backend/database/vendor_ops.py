""" ops specific to vendors """
from backend.models.vendor import Vendor
import json


def remove_password(vendors: list) -> list:
    """ exclude password hash from the vendor data """
    vendors_json = []
    for vendor in vendors:
        data = json.loads(vendor.to_json())
        data.pop('password')
        vendors_json.append(data)
    
    return vendors_json

def get_top_vendors(limit: int=None) -> list:
    """ get top selling products, ordered by rating """
    tops = Vendor.objects().order_by('-rating').limit(limit)
    vendors_without_password = remove_password(tops)
    return vendors_without_password

def get_single_vendor(email: str=None) -> dict:
    """ retrieve a single object based on its id """
    vendor = Vendor.objects(email=email).first()
    vendor_without_password  = remove_password([vendor])  # function expects list
    return vendor_without_password
