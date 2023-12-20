""" module to handle auth """
from flask import request, jsonify
from flask_login import login_user, logout_user, login_required, current_user
from mongoengine.errors import NotUniqueError
from pymongo.errors import DuplicateKeyError

from backend.custom_errors import *

from backend.auth import auth_views, login_manager
from backend.auth.utils import *
from backend.models.user import User, register_user

import bcrypt


@auth_views.route('signup', methods=['POST'], strict_slashes=False)
def signup():
    """ New user signup """
    if request.args:
        data = request.args()
    if request.form:
        data = request.form.to_dict()
        print(data)
    elif request.json:
        data = request.json

    error = "error"
    user = None

    data.update({"password": hash_password(data['password'])})
    try:
        user = register_user(**data)
    except (DuplicateKeyError, NotUniqueError):
        error = "email previosly registered"
    except DuplicateVendorError():
        error = "user is registered as vendor"
    
    if user:
        return jsonify({
            "status": "sucess",
            "message": "Sign up successful",
            "user": {
                "id": user.id,
                "email": email
            }
        }, 200)

    return jsonify({
        "status": "error",
        "message": "Sign up unsuccessful",
        "error": error
    }, 405)

@login_manager.user_loader
def load_user(user):
    return(User.objects(_cls='User', email=user.emaiil).first())

@auth_views.route('login', methods=['POST'], strict_slashes=False)
def login():
    """ Log in existing user """
    if request.args:
        email = request.args.get('email')
        password = request.args.get('password')
    elif request.form:
        email = request.form.get('email')
        password = request.form.get('password')
    elif request.json:
        email = request.json.get('email')
        password = request.json.get('password')
    else:
        return jsonify({
            "status": "unsucessful",
            "error": "couldn't retrieve data",
            "message": "invalid request format"
        })
    print(email, password)
    # retreive user
    user = User.objects(email=email).first()
    if user:
        if verify_password(password, user.password):
            login_user(user, remember=True)

            return jsonify({
                "status": "success",
                "message": "logged in successfully",
                "email": email
            }, 200)

        else:
            return jsonify({
            "status": "unsucessful",
            "message": "login unsuccessful",
            "error": "username or password incorrect"
        }, 403)

    else:
        return jsonify({
            "status": "unsucessful",
            "message": "login unsuccessful",
            "error": "username or password incorrect"
        }, 403)

    # return ('Log In')

@auth_views.route('logout', strict_slashes=False)
@login_required
def logout():
    logout_user()
    return ('Logout')

@auth_views.route('hello', strict_slashes=False)
@login_required
def hello():
    print(f"I am {current_user.firstname} and I am logged in")
    return current_user
