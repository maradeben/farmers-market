#!/usr/bin/env python3.9

from backend.models.vendor import Vendor
# from backend.database import file_store
from backend.database.vendor_ops import *
from backend.api.v1.views import app_views
from flask import jsonify, request


@app_views.route('vendors/top-vendors', methods=['GET'], strict_slashes=False)
def top_vendors():
    """ return top vendors """
    limit = int(request.args.get('limit', 20))
    return jsonify(get_top_vendors(limit))

@app_views.route('vendors/vendor/<vendor_id>', methods=['GET'], strict_slashes=False)
def single_vendor(vendor_id: str):
    """ retrieve a single vector by id """
    try:
        return jsonify(get_single_vendor(vendor_id))
    except KeyError:
        abort(404, description="Vendor not found")
