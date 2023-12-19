""" module to handle farmer auth """
from backend.api.v1.views import auth_views
# from backend.api.v1.views import app_views
import bcrypt
from flask import request, jsonify



@auth_views.route('signup', methods=['POST'], strict_slashes=False)
def signup():
    """ New user signup """
    params = request.args.to_dict()
    return ('Sign Up')

@auth_views.route('login', methods=['POST'], strict_slashes=False)
def login():
    return ('Log In')

@auth_views.route('logout', methods=['POST'], strict_slashes=False)
def logout():
    return ('Logout')
