#!/usr/bin/env python3.9from backend.api.v1.views import app_views

from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
auth_views = Blueprint('auth_views', __name__, url_prefix='/auth')

from backend.api.v1.views.product import *
from backend.api.v1.views.vendor import *
from backend.api.v1.views.auth import *
