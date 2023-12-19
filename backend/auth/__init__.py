from flask import Blueprint
from flask_login import LoginManager

# Blueprint for auth module
auth_views = Blueprint('auth_views', __name__, url_prefix='/auth')

# LoginManager instance
login_manager = LoginManager()
# configure LoginManager
login_manager.login_view = 'auth_views.login'
login_manager.login_message_category = 'info'

from backend.auth.auth import *
