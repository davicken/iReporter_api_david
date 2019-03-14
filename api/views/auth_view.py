from flask import request, Blueprint, make_response
from api import app
from api.controllers.users_controller import UsersController

authb_print = Blueprint("auth_view", __name__, url_prefix="/api/v1/auth")
user_obj = UsersController()

# update user to admin
@authb_print.route('/<user_id>/is_admin', methods=['PATCH'])
def edit_user_role_to_admin(user_id):
    return user_obj.make_user_admin(user_id)
    
@authb_print.route('/login', methods=["GET", "POST"])
def login_user():
    # method for logging in a user
    return user_obj.login()
   