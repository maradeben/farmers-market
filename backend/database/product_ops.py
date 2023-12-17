""" contains database operations relating to the products """
from backend.models.product import Product, product_categories


def get_products():
    """ retrieve all products from the database """
    return Product.objects()
