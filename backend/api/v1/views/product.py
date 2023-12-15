#!/usr/bin/env python3.9

from backend.models.product import Product, products_list, product_categories
from backend.database.file_storage import file_store
from backend.api.v1.views import app_views
from flask import jsonify

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def categories():
    """ return product categories """
    return jsonify(product_categories)

@app_views.route('/all_products', methods=['GET'], strict_slashes=False)
def all_products():
    """ return all products """
    return jsonify(file_store.all())