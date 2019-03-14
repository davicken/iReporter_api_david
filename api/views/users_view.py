from flask import request, Blueprint
from api import app
from api.controllers.users_controller import UsersController

ub_print = Blueprint("users_view", __name__, url_prefix="/api/v1/users")
user_obj = UsersController()

# create a new user end-point
@ub_print.route('', methods=['POST'])
def register_new_user():
    return user_obj.create_user()

# get all users end-point
@ub_print.route('', methods=['GET'])
def get_all_created_users():
    return user_obj.get_all_users()

# get a single user by his id endpoint
@ub_print.route('/<user_id>', methods=['GET'])
def get_specific_redflag(user_id):
    return user_obj.get_user(user_id)

# delete a single user record by its id endpiont
@ub_print.route('/<user_id>', methods=['DELETE'])
def delete_specific_user_record(user_id):
    return user_obj.delete_user(user_id)

# edit specific user record  endpoint
@ub_print.route('/<user_id>', methods=['PATCH'])
def edit_specific_user_info(user_id):
    return user_obj.edit_user(user_id)

