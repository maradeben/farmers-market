#!/usr/bin/env python3.9

# from backend.models.product import Product, product_categories
# from backend.database import file_store
from backend.api.v1.views import app_views

from backend.database.product_ops import *

from flask import jsonify

@app_views.route('products/categories', methods=['GET'], strict_slashes=False)
def categories():
    """ return product categories """
    return jsonify(product_categories)

# @app_views.route('products/all_products', methods=['GET'], strict_slashes=False)
# def all_objects():
#     """ return all products """
#     return jsonify(file_store.all())

@app_views.route('products/top-selling', methods=['GET'], strict_slashes=False)
def top_selling():
    """ return the top selling products """
    return get_products()

@app_views.route('/products/', methods=['GET'], strict_slashes=False)
@app_views.route('/products/<cat_name>', methods=['GET'], strict_slashes=False)
def products(cat_name=None):
    """ retrieve products of a particular category """
    return jsonify(file_store.get_products(cat_name))

@app_views.route('/products/product/<product_id>', methods=['GET'], strict_slashes=False)
def single_product(product_id: str):
    """ return a single product based on the id passed """
    try:
        return jsonify(file_store.get_single_product(product_id))
    except KeyError:
        abort(404, description="Product not found")
