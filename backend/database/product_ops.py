""" contains database operations relating to the products """
from backend.models.product import Product, product_categories
import json


# map routes to corresponding categories
cat_routes = {
    'fruits-veggies': 'Fruits/Vegetables',
    'grains': 'Grains',
    'oils': 'Oils',
    'meat-poultry': 'Meat/Poultry',
    'roots-tubers': 'Roots/Tubers'
}


def include_vendor_location(products: list) -> list:
    """ retrieve and include vendor locations to objects """

    products_json = []
    for product in products:
        data = json.loads(product.to_json())
        data.update({'location': product.vendor.location})
        products_json.append(data)
    
    return products_json

def get_products(category: str=None) -> list:
    """ retrieve all products from the database """

    if category:
        category = cat_routes[category]
        products = Product.objects(category=category)
    else:
        products = Product.objects()

    # include location
    products_with_loc = include_vendor_location(products)
    
    return products_with_loc

def get_top_products(limit: int=None) -> list:
    """ get top selling products, ordered by rating """
    tops = Product.objects().order_by('-rating').limit(limit)

    tops_with_loc = include_vendor_location(tops)
    return tops_with_loc

def get_single_product(id: str=None) -> dict:
    """ retrieve a single object based on its id """
    product = Product.objects(id=id).first()
    product_with_loc = include_vendor_location([product])  # function expects list
    return product_with_loc
